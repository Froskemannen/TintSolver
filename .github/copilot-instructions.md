# Central Copilot Instructions file for VS Code

## Overview
This file summarizes the main Copilot policies for this repository. For detailed instructions, see the relevant files in the `instructions/` folder.

- Command line access: see `instructions/command-line.instructions.md`
- Code edits: see `instructions/edits.instructions.md`
- Markdown: see `instructions/markdown.instructions.md`
- Label Studio config: see `instructions/label_studio_config.instructions.md`
- Labeled data export: see `instructions/labeled_data_export.instructions.md`
- Cache DB: see `instructions/cache_db.instructions.md`
- Requirements: see `instructions/requirements.instructions.md`
- Shell scripts: see `instructions/shell_scripts.instructions.md`

## Source Control and Branching

# Copilot Source Control Instructions

Repository is Froskemannen/TintVision

- Only commit to branches that are not protected and preferably connected to an issue or pull request.
- Reference the issue number in commit messages when working on an issue.
- Use clear, conventional commit messages.
- Avoid committing generated or temporary files unless explicitly required.
- For issue-specific work, use or create an `issue-*-*.md` file for tracking.

## Working with Issues

# Copilot Issues Instructions

- When working on an issue, always reference the issue number in your commit messages and code comments where relevant.
- Use the `issue-*-*.md` file for the issue you are working on. If none exists, create one with the appropriate name and description.
- Document progress and decisions in the relevant issue file or in `DEVLOG.md` if broader context is needed.
- Close issues only when all acceptance criteria are met and documented.

## Documentation and Project Notes

# Copilot Documentation and Project Notes Instructions

- Do not auto-edit documentation files unless explicitly requested by the user.
- Preserve the structure and intent of `NOTES.md`, `DEVLOG.md`, and `README.md` files.
- For configuration files like `label_studio_config.xml`, only make changes when the user provides clear instructions.
- When updating documentation, keep user-facing and contributor-facing information clearly separated.
- Reference design decisions and rationale in `NOTES.md` and log chronological changes in `DEVLOG.md`.

## Writing Copilot Instructions
For guidance on writing or maintaining Copilot instruction files, see `.github/instructions/writing_copilot_instructions.md`.

> **Note:**
> `.github/instructions/writing_copilot_instructions.md` is for instruction authors only. It must NOT be used as a general Copilot instruction file for code generation, review, commit messages, or other automated tasks. Exclude it from any `applyTo` patterns or settings that would cause Copilot to use it for those purposes.

### Quick Reference {#quick_reference}

#### Command Line Access
See `instructions/command-line.instructions.md` for details.

#### Edits
See `instructions/edits.instructions.md` for details.

#### Markdown
See `instructions/markdown.instructions.md` for details.

#### Label Studio Config
See `instructions/label_studio_config.instructions.md` for details.

#### Labeled Data Export
See `instructions/labeled_data_export.instructions.md` for details.

#### Cache DB
See `instructions/cache_db.instructions.md` for details.

#### Requirements
See `instructions/requirements.instructions.md` for details.

#### Shell Scripts
See `instructions/shell_scripts.instructions.md` for details.