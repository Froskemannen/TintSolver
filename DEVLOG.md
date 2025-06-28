# Development Log (DEVLOG.md)

This file contains a chronological log of development activities, experiments, and decisions for this project.

---

## 2025-06-26: Migrating Issue #3 Notes

Migrated key content from `issue-3-foundation-model.md` to this log for future reference. See below for details.

---

### Issue #3: Integrate Foundation Model (SAM or Grounding DINO)

**Summary:**
Integrate a foundation segmentation model (e.g., SAM or Grounding DINO) into the ML backend’s `predict` method to auto-generate masks for known prompts.

**Steps:**

1. Install and set up the foundation model (SAM or Grounding DINO).
2. Modify `my_ml_backend/model.py` to use the model in the `predict` method.
3. Ensure predictions are returned in the Label Studio format.
4. Test the integration using `test_api.py`.
5. Document any setup or usage instructions in `README.md`.

**References:**

* <https://labelstud.io/guide/ml>
* <https://github.com/facebookresearch/segment-anything>
* <https://github.com/IDEA-Research/GroundingDINO>

**Acceptance Criteria:**

* [ ] Foundation model is installed and callable from backend
* [ ] `predict` method returns valid masks for prompts
* [ ] Integration is tested and documented

**Update 2025-06-25:**

* The backend now checks for the existence of the SAM checkpoint file in `model.py` and raises a clear error if it is missing, with instructions for setting the correct path via the `SAM_CHECKPOINT` environment variable.
* To proceed with testing or running the backend, you must provide a valid SAM checkpoint file (e.g., `sam_vit_h.pth`) and set the environment variable accordingly.
* Example:

  ```bash
  export SAM_CHECKPOINT=/absolute/path/to/sam_vit_h.pth
  ```
  
* If the checkpoint is missing, the backend will not start and will print a descriptive error message.
* This change ensures that anyone running the backend or tests will immediately know how to resolve the issue.

---

(See `issue-3-foundation-model.md` for the full original issue and implementation details.)
