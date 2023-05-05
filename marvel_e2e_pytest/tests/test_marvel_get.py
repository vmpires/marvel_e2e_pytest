import requests
from marvel_e2e_pytest.tools.helpers import ENDPOINT


# Happy path
def test_get_all_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    pass

# Happy path
def test_get_one_endpoint_valid():
    hero_id = 1
    response = requests.get(ENDPOINT + f"/{hero_id}")
    
    assert response.status_code == 200
    assert "id" in response.json()

    keys_to_check = ["id", "name", "attack", "defense", "life"]
    assert all(key in response.json() for key in keys_to_check)
    pass


def test_get_one_endpoint_valid():
    hero_id = 100
    response = requests.get(ENDPOINT + f"/{hero_id}")
    
    assert response.status_code == 404