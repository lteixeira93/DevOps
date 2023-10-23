from utils.myconfigparser import get_pet_api_url

BASE_URL_PET_STORE = get_pet_api_url()


def test_a1():
    assert 5 + 5 == 10


# def test_a2():
#     assert 9 / 5 == 1.5, "Failed intentionally"


def test_a3():
    url = BASE_URL_PET_STORE + '123'
    print(url)
    assert 'petstore' in url
