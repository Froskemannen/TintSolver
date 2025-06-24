# Issue-Driven Development with Git Flow (Optimized for Solo Devs & Copilot)

This document combines insights from [Mattchine's Gist](https://gist.github.com/Mattchine/176ca6a0c7cd3eaa442dd9d7559ad2f9) and [nvie.com's successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/) with a clean, Copilot-friendly ASCII diagram.

---

## 🔧 Overview

**Issue-driven development** links every feature, fix, or change to a specific GitHub issue. The Git branching model ensures clean separation of work, stable releases, and clear traceability.

We optimize Git Flow for solo or small-team devs with test-first habits and GitHub Copilot usage.

---

## 🌿 Git Branching Flow (Optimized)

```
main ←─────●─────●─────────────────────●─────●─────●───→ # production-ready tags
            (v1)   (v2)                (v3)

            ↑       ↑ (hotfix)            ↑ (hotfix)
            │       │                     │
         hotfix   hotfix                hotfix
            │       │                     │
develop ←───┴───●───┴───●───●───●─────●───┴───●───●───●───→ develop
            ↑       ↑       ↑        ↑       ↑    ↑
         feature branches for new features or bugfixes
```

### 📘 Legend

- `main`: Production-ready, stable versions (tagged)
- `develop`: Integration branch, staging for release
- `feature/*`: One branch per issue, short-lived
- `release/*`: Prep branch to stabilize before tagging
- `hotfix/*`: Emergency fixes branched from `main`

### 🔁 Merge Strategy

| From → To               | Purpose                         |
| ----------------------- | ------------------------------- |
| `feature/*` → `develop` | Merge completed feature work    |
| `develop` → `release/*` | Create a release candidate      |
| `release/*` → `main`    | Finalize and tag a release      |
| `release/*` → `develop` | Back-merge final changes        |
| `hotfix/*` → `main`     | Patch production directly       |
| `hotfix/*` → `develop`  | Sync emergency fix into develop |

---

## ✅ Step-by-Step Workflow

### 1. Start a New Issue

- Open a GitHub Issue (e.g. `#42` Improve login UX)
- Create a branch: `feature/42-login-ux`

```bash
git checkout develop
git checkout -b feature/42-login-ux
```

### 2. Develop with Tests

- Follow test-first methodology
- Commit regularly with clear messages

```bash
git add .
git commit -m "[#42] Add initial login UX tests"
```

### 3. Merge Feature

- Open a PR from `feature/42-login-ux` → `develop`
- Merge once approved or complete

### 4. Create a Release

```bash
git checkout develop
git checkout -b release/1.0.0
```

- Final tests, docs, minor tweaks

### 5. Release to Production

```bash
git checkout main
git merge release/1.0.0
git tag v1.0.0
```

- Then back-merge to develop:

```bash
git checkout develop
git merge release/1.0.0
```

### 6. Hotfix (if needed)

```bash
git checkout main
git checkout -b hotfix/1.0.1
# Fix bug, then:
git commit -m "Hotfix: patch crash on login"
git checkout main
git merge hotfix/1.0.1
git tag v1.0.1
git checkout develop
git merge hotfix/1.0.1
```

---

## 🤖 Copilot & Prompting Tips

- Keep branch names descriptive and issue-linked
- Write small, testable commits: Copilot will infer purpose better
- Use comments in code like:
  ```js
  // TODO: #42 Implement login state persistence
  ```
- Prompt Copilot with file-aware context:
  > "Finish login flow from feature/42-login-ux branch"

---

## 🔗 References

- [nvie.com: A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)
- [Mattchine: issue\_driven\_development.md](https://gist.github.com/Mattchine/176ca6a0c7cd3eaa442dd9d7559ad2f9)
- [Git Flow cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/)

---
