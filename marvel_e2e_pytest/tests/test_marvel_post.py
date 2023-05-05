
# Happy path
from marvel_e2e_pytest.tools.helpers import create_hero, delete_hero, generate_invalid_new_hero, generate_valid_new_hero, get_hero


def test_create_endpoint_valid():
    payload = generate_valid_new_hero()
    create_response = create_hero(payload)
    
    assert create_response.status_code == 201

    data = create_response.json()
    hero_id = data["id"]
    get_response = get_hero(hero_id)
    
    assert get_response.status_code == 200
    assert get_response.json()["id"] == hero_id
    
    delete_hero(hero_id)


def test_create_endpoint_invalid():
    payload = generate_invalid_new_hero()
    create_response = create_hero(payload)
    
    assert create_response.status_code == 500