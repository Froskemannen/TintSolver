from typing import List, Dict, Optional
from label_studio_ml.model import LabelStudioMLBase
from label_studio_ml.response import ModelResponse

# TODO: Import your foundation model here (e.g., SAM, Grounding DINO)
# Example:
# from segment_anything import SamPredictor, sam_model_registry
# import torch

class NewModel(LabelStudioMLBase):
    """Custom ML Backend model with foundation model integration (SAM or Grounding DINO)
    """
    def setup(self):
        """Configure any parameters of your model here, including loading the foundation model"""
        self.set("model_version", "0.0.1")
        # TODO: Load your foundation model here
        # Example:
        # self.sam = sam_model_registry["vit_h"](checkpoint="/path/to/sam_vit_h.pth")
        # self.predictor = SamPredictor(self.sam)
        # self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # self.sam.to(self.device)

    def predict(self, tasks: List[Dict], context: Optional[Dict] = None, **kwargs) -> ModelResponse:
        """
        Run prediction using the foundation model.
        :param tasks: [Label Studio tasks in JSON format](https://labelstud.io/guide/task_format.html)
        :param context: [Label Studio context in JSON format](https://labelstud.io/guide/ml_create#Implement-prediction-logic)
        :return: ModelResponse(predictions=predictions) with predictions in Label Studio format
        """
        print(f"""
        Run prediction on {tasks}
        Received context: {context}
        Project ID: {self.project_id}
        Label config: {self.label_config}
        Parsed JSON Label config: {self.parsed_label_config}
        Extra params: {self.extra_params}""")

        predictions = []
        for task in tasks:
            # TODO: Extract image path or data from task
            # Example:
            # image_path = task['data']['image']
            # prompt = ... # Extract prompt from task/context if needed

            # TODO: Run foundation model inference
            # Example:
            # mask = self.predictor.predict(image_path, prompt)

            # TODO: Convert mask to Label Studio result format
            # result = ...
            # predictions.append({
            #     "model_version": self.get("model_version"),
            #     "result": [result]
            # })
            pass

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

