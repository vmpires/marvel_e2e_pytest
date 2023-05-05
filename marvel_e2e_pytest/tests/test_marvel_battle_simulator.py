
# Happy path
from marvel_e2e_pytest.tools.helpers import battle, invalid_battle


def test_valid_battle_endpoint():
    battle_response = battle(1,2)
    assert battle_response.status_code == 200
    pass

def test_invalid_battle_endpoint():
    battle_response = battle(1,100)
    assert battle_response.status_code == 404
    pass

def test_battle_endpoint():
    battle_response = invalid_battle(1,2)
    assert battle_response.status_code == 200
    assert battle_response.json() == {"error": "hero1 or hero2 parameter missing..."}
    pass