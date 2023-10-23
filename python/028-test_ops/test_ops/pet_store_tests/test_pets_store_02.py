import json

import pytest
from utils.myconfigparser import get_pet_api_url
from utils.apiutils import get_api_data, post_api_data

base_url = get_pet_api_url()

# From https://petstore.swagger.io/#/pet/findPetsByStatus
test_data = [
    ("available", 200),
    ("pending", 200),
    ("sold", 200),
]


# Execute several data within same test
@pytest.mark.parametrize("test_type, status", test_data)
def test_get_pet_by_status(test_type, status):
    url = base_url + "findByStatus"
    print("(test_get_pet_by_status) URL: " + url)
    params = {test_type: status}
    print(params)
    response = get_api_data(url, params=params)
    assert response.status_code == status
    print(response.json())
