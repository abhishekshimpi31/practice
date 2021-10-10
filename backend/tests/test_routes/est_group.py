from tests.conftest import normal_user_token_headers
import json


def test_create_group(client,normal_user_token_headers):
    data = {"name": "group1",
            "description": "First Group",
            "devices": "Mobile, Phone",
            "created_by": "user1",
            "updated_by": "user1",
            "created_on": "2021-09-18",
            "updated_on": "2021-09-18"}
    response = client.post("/devicegroup/create", data=json.dumps(data), headers=normal_user_token_headers)
    assert response.status_code == 200
#     assert response.json()["name"] == "group1"
#     assert response.json()["description"] == 'First Group'
#     assert response.json()["devices"] == 'Mobile, Phone'

