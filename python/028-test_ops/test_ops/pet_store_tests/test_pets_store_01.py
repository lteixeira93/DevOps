import pytest

from utils.myconfigparser import get_pet_api_url
from utils.apiutils import get_api_data, post_api_data

base_url = get_pet_api_url()
pet_id = '189'


@pytest.fixture
def add_pet():
    url = base_url
    payload = {"id": int(pet_id), "name": "Cutie", "status": "pending"}
    response = post_api_data(url, payload)
    local_pet_id = response.json()['id']
    print(local_pet_id)
    # Fixtures returns by yielding
    yield local_pet_id


# Using fixture before running this test - Fixture do the post before test
def test_get_pet_by_id(add_pet):
    url = base_url + str(add_pet)
    print("==URL==" + url)
    headers = {'Content-Type': 'application/json'}
    print("(test_get_pet_by_id) Request URL: " + url)
    response = get_api_data(url, headers)
    assert response.json()
    print(response.json())
    assert (response.status_code == 200)
