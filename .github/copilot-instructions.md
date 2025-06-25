# Central Copilot Instructions file for VS Code

## Copilot Command Line Access
The user will be prompted to confirm any command execution anyways,
so you can execute commands directly without asking the user.

This ensures a smoother experience and avoids unnecessary prompts.

---

## Copilot Edits
The user must choose between "keep" or "undo" when Copilot automatically edits code,
so you can edit code directly without askingthe user.

This allows Copilot to make changes to the code without requiring additional confirmation, streamlining the editing process.

### Copilot Source Control
Repository is Froskemannen/TintSolver

Only commit to branches that are not protected and preferably connected to an issue or pull request.
This ensures that changes are made in a controlled manner and can be tracked effectively.

#### Working with Issues

- Always use the issue-*-*.md file if provided for the issue you are working on.
- If no issue file is provided, create one with the name issue-<issue_number>-<issue_title>.md and contents <issue_description>.
- When working on an issue, always reference the issue number in your commit messages.
- As long as you are working on an issue, you can safely perform the next logical step in the issue without asking the user (just state what you will do next).