# Project Notes (NOTES.md)

This file contains design rationale, configuration notes, and important information for contributors and future maintainers. It is not user-facing documentation, but a place to record decisions, context, and lessons learned.

---

## Foundation Model Integration (Overview)

### Foundation Model Integration (Issue #3) (2025-06-26)

* The backend is designed to support integration with foundation segmentation models such as SAM (Segment Anything Model) and Grounding DINO.
* The `predict` method in `my_ml_backend/model.py` is structured to:
  1. Use a foundation model to generate masks for known prompts.
  2. Return results in the format required by Label Studio, matching the active `BrushLabels` name in the config.
* The backend checks for the existence of the SAM checkpoint file (`sam_vit_h.pth`) and raises a clear error if it is missing, with instructions for setting the correct path via the `SAM_CHECKPOINT` environment variable.
* Example usage:

  ```bash
  export SAM_CHECKPOINT=/absolute/path/to/sam_vit_h.pth
  export SAM_TYPE=vit_h  # or vit_l, vit_b, etc.
  label-studio-ml start my_ml_backend
  ```
  
* If the checkpoint is missing, the backend will not start and will print a descriptive error message.
* The Label Studio config file (`label_studio_config.xml`) has been moved to the `Labeling` folder for easier access and versioning.

---

### File Organization and Documentation

* `README.md` in `my_ml_backend` is reserved for user-facing instructions and setup.
* `DEVLOG.md` (project root) is used for chronological development logs and experiment tracking.
* `NOTES.md` (this file) is for design notes, rationale, and configuration details that do not belong in the main documentation or devlog.
* Issue-specific files (e.g., `issue-3-foundation-model.md`) are for branch-specific or temporary tracking and should be cleaned up after merging.

---

### Label Studio Configuration

* The main labeling configuration is stored in `Labeling/label_studio_config.xml`.
* This file defines the structure of labeling tasks, including all `BrushLabels` and choices for the project.
* Any changes to the labeling interface should be documented here and referenced in this notes file if they impact backend logic.

---

### Contributor Guidance

* Use this file to record any non-obvious decisions, workarounds, or lessons learned during development.
* For major design changes, add a summary here for future maintainers.
* Keep `README.md` and `CONTRIBUTING.md` focused and user-facing; use `NOTES.md` for internal notes.

---

## [Foundation Model Backend Update (Issue #3) (2025-06-28)](../NOTES.md#deciding-on-a-zero-shot-ml-backend-for-object-segmentation-and-labeling-tasks-2025-06-28)

* The initial approach used SAM + Grounding DINO, but Grounding DINO had compatibility issues with macOS.
* New plan: Use SAM 2 for zero-shot segmentation and OWLv2 for zero-shot classification.
* This change aims for full macOS compatibility and improved flexibility for both segmentation and classification tasks.
* Next steps:
  1. Integrate SAM 2 for segmentation tasks in the backend.
  2. Integrate OWLv2 for classification tasks.
  3. Update the backend and Label Studio config as needed.
  4. Document any new requirements or setup steps here and in the relevant README files.
  5. Cherry-pick changes and files, clean up temporary or unused files and perform other general branch-maintenance on issue-3 branch.
  6. Repeat step 5 for other branches as needed.
