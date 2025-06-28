# Brainstorming Notes and Next Steps for TintVision

## Deciding on a zero-shot ML Backend for Object Segmentation and Labeling Tasks (2025-06-28)

Since there were some issues with the initial implementation of the zero-shot ML backend—specifically, the compatibility issues with Grounding DINO and macOS—let's consider a new approach that is fully compatible with macOS and can handle both segmentation and classification tasks effectively.

1. Marry SAM 2 with OWLv2 (second place after Grounding DINO) within a new label-studio-ml-backend.
2. Let SAM 2 handle the zero-shot segmentation tasks.
3. Use OWLv2 for the zero-shot classification tasks.
