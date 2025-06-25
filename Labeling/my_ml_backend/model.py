from typing import List, Dict, Optional
from label_studio_ml.model import LabelStudioMLBase
from label_studio_ml.response import ModelResponse

# Import SAM (Segment Anything Model) dependencies
from segment_anything import SamPredictor, sam_model_registry, SamAutomaticMaskGenerator
import torch
import numpy as np
from PIL import Image
import os
from skimage import measure

# TODO: Ensure that the predict method returns results with 'from_name' matching the active BrushLabels name
# (e.g., 'target_butterfly', 'target_frog', or 'target_flower') and 'to_name' set to 'image',
# and outputs a mask in the format required by BrushLabels (base64-encoded PNG or RLE),
# to be compatible with the current Label Studio XML config (now using BrushLabels/masks, not polygons).
# See Labeling/my_ml_backend/label_studio_config.xml for the current labeling configuration.
# Reference: Issue #3 (foundation model integration, mask output)

class NewModel(LabelStudioMLBase):
    """Custom ML Backend model with foundation model integration (SAM)"""
    def setup(self):
        self.set("model_version", "0.1.0-sam")
        sam_checkpoint = os.environ.get("SAM_CHECKPOINT", "/path/to/sam_vit_h.pth")
        sam_type = os.environ.get("SAM_TYPE", "vit_h")
        if not os.path.isfile(sam_checkpoint):
            raise FileNotFoundError(
                f"SAM checkpoint not found at '{sam_checkpoint}'. "
                "Please set the SAM_CHECKPOINT environment variable to the correct path of your .pth file. "
                "See README.md for details."
            )
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.sam = sam_model_registry[sam_type](checkpoint=sam_checkpoint)
        self.sam.to(self.device)

    def predict(self, tasks: List[Dict], context: Optional[Dict] = None, **kwargs) -> ModelResponse:
        """
        Run prediction using the foundation model.
        :param tasks: [Label Studio tasks in JSON format](https://labelstud.io/guide/task_format.html)
        :param context: [Label Studio context in JSON format](https://labelstud.io/guide/ml_create#Implement-prediction-logic)
        :return: ModelResponse(predictions=predictions) with predictions in Label Studio format
        """
        predictions = []
        mask_generator = SamAutomaticMaskGenerator(self.sam)
        for task in tasks:
            try:
                # Extract image path from task
                image_path = task['data']['image']
                image = np.array(Image.open(image_path).convert("RGB"))
                masks = mask_generator.generate(image)
                results = []
                for mask_data in masks:
                    mask = mask_data["segmentation"]
                    contours = measure.find_contours(mask, 0.5)
                    polygons = []
                    for contour in contours:
                        # Convert (row, col) to (x, y) pairs for Label Studio
                        polygon = [float(coord) for row, col in contour for coord in (col, row)]
                        if len(polygon) >= 6:  # At least 3 points
                            polygons.append(polygon)
                    if not polygons:
                        continue
                    results.append({
                        "from_name": "label",
                        "to_name": "image",
                        "type": "polygon",
                        "value": {
                            "points": [list(np.array(p).reshape(-1, 2).tolist()) for p in polygons],
                            "polygonlabels": ["object"]
                        }
                    })
                predictions.append({
                    "model_version": self.get("model_version"),
                    "result": results
                })
            except (IOError, OSError) as e:
                print(f"File error in prediction: {e}")
                continue
            except Exception as e:
                print(f"Unexpected error in prediction: {e}")
                raise
        return ModelResponse(predictions=predictions)

    def fit(self, event, data, **kwargs):
        """
        This method is called each time an annotation is created or updated
        You can run your logic here to update the model and persist it to the cache
        It is not recommended to perform long-running operations here, as it will block the main thread
        Instead, consider running a separate process or a thread (like RQ worker) to perform the training
        :param event: event type can be ('ANNOTATION_CREATED', 'ANNOTATION_UPDATED', 'START_TRAINING')
        :param data: the payload received from the event (check [Webhook event reference](https://labelstud.io/guide/webhook_reference.html))
        """

        # use cache to retrieve the data from the previous fit() runs
        old_data = self.get('my_data')
        old_model_version = self.get('model_version')
        print(f'Old data: {old_data}')
        print(f'Old model version: {old_model_version}')

        # store new data to the cache
        self.set('my_data', 'my_new_data_value')
        self.set('model_version', 'my_new_model_version')
        print(f'New data: {self.get("my_data")}')
        print(f'New model version: {self.get("model_version")}')

        print('fit() completed successfully.')

