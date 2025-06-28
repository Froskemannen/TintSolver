#!/bin/bash

# Find untracked files and stage them with intent-to-add, saving their names
untracked_files=$(git ls-files --others --exclude-standard)
if [ -n "$untracked_files" ]; then
  echo "$untracked_files" | xargs -r git add --intent-to-add
fi

# Helper: map short status to full name
status_name() {
  case "$1" in
    A) echo "Added";;
    M) echo "Modified";;
    D) echo "Deleted";;
    R*) echo "Renamed";;
    C*) echo "Copied";;
    U) echo "Unmerged";;
    T) echo "Type Changed";;
    *) echo "$1";;
  esac
}

# Get staged and unstaged changes
staged=$(git diff --cached --name-status develop)
unstaged=$(git diff --name-status develop)

# Collect all files with their status and stage info
all_changes=""
if [ -n "$staged" ]; then
  while IFS=$'\t' read -r status file; do
    if echo "$untracked_files" | grep -qx "$file"; then
      all_changes+="Untracked\tStaged\t$status\t$file\n"
    else
      all_changes+="Tracked\tStaged\t$status\t$file\n"
    fi
  done <<< "$(echo "$staged" | awk '{print $1 "\t" $2}')"
fi
if [ -n "$unstaged" ]; then
  while IFS=$'\t' read -r status file; do
    if echo "$untracked_files" | grep -qx "$file"; then
      all_changes+="Untracked\tUnstaged\t$status\t$file\n"
    else
      all_changes+="Tracked\tUnstaged\t$status\t$file\n"
    fi
  done <<< "$(echo "$unstaged" | awk '{print $1 "\t" $2}')"
fi

# Pretty print: group by Tracked/Untracked, then Staged/Unstaged, then status
printf "%b" "$all_changes" | sort -k1,1 -k2,2 -k3,3 -k4,4 | awk '
  function status_name(s) {
    if (s ~ /^A$/) return "Added";
    if (s ~ /^M$/) return "Modified";
    if (s ~ /^D$/) return "Deleted";
    if (s ~ /^R/) return "Renamed";
    if (s ~ /^C/) return "Copied";
    if (s ~ /^U$/) return "Unmerged";
    if (s ~ /^T$/) return "Type Changed";
    return s;
  }
  BEGIN { outer=""; stage=""; status="" }
  $1 != outer {
    if (outer != "") print "\n";
    outer = $1;
    print "==== " outer " ====\n";
    stage=""; status="";
  }
  $2 != stage {
    if (stage != "") print "\n";
    stage = $2;
    print "  === " stage " ===\n";
    status="";
  }
  # For Untracked/Unstaged, print files with (added) and skip status header
  ($1=="Untracked" && $2=="Unstaged") {
    print "      - " $4 " (added)";
    next;
  }
  # For other groups, print status header if changed
  $3 != status {
    if (status != "") print "\n";
    status = $3;
    print "    == " status_name(status) " ==\n";
  }
  { print "      - " $4 }
'

# Unstage the files that were just staged (if any)
if [ -n "$untracked_files" ]; then
  echo -e "\n\n========================================\n"
  echo "$untracked_files" | xargs -r git reset
  echo -e "\n\n"
  # No extra summary printed here; only the pretty-printed summary above is shown
fi
