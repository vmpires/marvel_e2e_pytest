
from marvel_e2e_pytest.tools.helpers import create_hero, delete_hero, generate_valid_new_hero, update_hero


def test_update_endpoint_valid():
    payload = generate_valid_new_hero()
    create_response = create_hero(payload)
    
    assert create_response.status_code == 201

    hero_id = create_response.json()["id"]
    new_payload = {**generate_valid_new_hero(), "team": 0}
    update_response = update_hero(hero_id, new_payload)

    assert update_response.status_code == 200
    assert update_response.json()["id"] == hero_id
    assert update_response.json()["team"] == 'con_registry'

    delete_hero(hero_id)

def test_update_endpoint_invalid():
    payload = generate_valid_new_hero()
    create_response = create_hero(payload)
    hero_id = create_response.json()["id"]
    
    assert create_response.status_code == 201
    hero = {key: create_response.json()[key] for key in ["name", "attack", "defense", "life", "team"]}
    hero["attack"] = "string"

    update_response = update_hero(hero_id, hero)
    assert update_response.status_code == 422