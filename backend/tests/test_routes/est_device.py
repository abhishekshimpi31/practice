from starlette.testclient import TestClient
from tests.conftest import normal_user_token_headers
import json


def test_create_device(client,normal_user_token_headers):
    data = {"device_ip": "204.120.0.16",
            "device_hostname": "device2",
            "device_location": "pune",
            "created_by": "user1",
            "updated_by": "user1",
            "created_on": "2021-09-18",
            "updated_on": "2021-09-18"}
    response = client.post("/device/create", data=json.dumps(data),headers=normal_user_token_headers)
    assert response.status_code == 200
#     assert response.json()["ip"] == "204.120.0.16"
#     assert response.json()["hostname"] == 'device2'
#     assert response.json()["updated_on"] == '2021-09-18'
