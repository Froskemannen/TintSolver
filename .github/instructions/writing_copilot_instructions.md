---
applyTo: '.github/instructions/*.instructions.md,.github/copilot-instructions.md'
---

# Copilot Instructions for Writing Instructions

This file provides guidance for writing Copilot instruction files in this repository. Always adhere to the following principles:

## Key Guidelines

1. **Reference the Customization Guide**
   - Use [docs/copilot-customization.md](../../docs/copilot-customization.md) as the primary source of guidance for writing and maintaining instruction files.

2. **Purpose of Instruction Files**
   - Instruction files should be concise, clear, and specific to their context.
   - Avoid redundancy by referencing other instruction files where applicable.

3. **File Naming and Placement**
   - Place instruction files in the `.github/instructions/` directory.
   - Use descriptive names that reflect the file's purpose (e.g., `test.instructions.md`, `labeling.instructions.md`).

4. **Maintenance**
   - Update instruction files as the project evolves.
   - Ensure consistency with the central instructions file located at `.github/copilot-instructions.md`.

5. **Avoid Creating Duplicate Files**
   - Always check if an instruction file already exists before creating a new one.
   - If a file exists, update it instead of creating a duplicate.

## Example Structure

```markdown
---
applyTo: '<file-pattern>'
---

# Title of the Instructions

## Section 1
- Guideline or rule 1
- Guideline or rule 2

## Section 2
- Additional details or examples
```

## Notes

- Instruction files should be written in Markdown and follow the structure outlined above.
- Use the `applyTo` metadata field to specify the files or directories the instructions apply to.
- Regularly review and update instruction files to reflect changes in project requirements or workflows.
