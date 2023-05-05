import requests
from marvel_e2e_pytest.tools.helpers import ENDPOINT, create_hero, generate_valid_new_hero


def test_delete_endpoint_valid():
    payload = generate_valid_new_hero()
    create_response = create_hero(payload)
    hero_id = create_response.json()["id"]

    assert create_response.status_code == 201

    delete_response = requests.delete(ENDPOINT + f"/{hero_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["deleted"]["id"] == hero_id

def test_delete_endpoint_invalid():
    hero_id = 100
    response = requests.delete(ENDPOINT + f"/{hero_id}")
    
    assert response.status_code == 404
    assert response.json() == {"error": f"Hero {hero_id} not found!"}