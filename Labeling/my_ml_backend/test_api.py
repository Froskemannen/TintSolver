"""
IMPORTANT: You must set the SAM_CHECKPOINT environment variable to a valid .pth checkpoint file for the Segment Anything Model (SAM) before running these tests.
Example:
    export SAM_CHECKPOINT=/absolute/path/to/sam_vit_h.pth
If the checkpoint is missing, the backend will raise a clear error and the test will fail.

This file contains tests for the API of your model. You can run these tests by installing test requirements:

    ```bash
    pip install -r requirements-test.txt
    ```
Then execute `pytest` in the directory of this file.

- Change `NewModel` to the name of the class in your model.py file.
- Change the `request` and `expected_response` variables to match the input and output of your model.
"""

from dotenv import load_dotenv

load_dotenv()

import os
import pytest
import json
from model import NewModel

SAM_CHECKPOINT = os.environ.get('SAM_CHECKPOINT', '/path/to/sam_vit_h.pth')


@pytest.fixture
def client():
    from _wsgi import init_app
    app = init_app(model_class=NewModel)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def test_image_path():
    from pathlib import Path
    # Adjust the path as needed to point to your test image
    return str((Path(__file__).parent.parent / "Labeling" / "Cropped" / "1-cropped.png").resolve())

@pytest.mark.skipif(not os.path.isfile(SAM_CHECKPOINT), reason=f"SAM checkpoint not found at {SAM_CHECKPOINT}. Set SAM_CHECKPOINT env variable to a valid .pth file.")
def test_predict(client, test_image_path):
    request = {
        'tasks': [{
            'data': {
                # Use a real local image from the dataset
                'image': test_image_path
            }
        }],
        # Minimal label config for polygon output
        'label_config': '''<View>
  <Image name="image" value="$image"/>
  <PolygonLabels name="label" toName="image">
    <Label value="object"/>
  </PolygonLabels>
</View>'''
    }

    # The expected result is a placeholder; update as needed after running the test
    expected_response = {
        'results': [
            # The actual output will depend on the model and image
        ]
    }

    response = client.post('/predict', data=json.dumps(request), content_type='application/json')
    assert response.status_code == 200
    response = json.loads(response.data)
    # For now, just check that results are present
    assert 'results' in response
    # Optionally, check that at least one result is returned
    assert isinstance(response['results'], list)
