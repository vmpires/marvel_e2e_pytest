import requests
from faker import Faker

fake = Faker()

ENDPOINT = "http://localhost:3000/heroes"

# Helper Functions

def generate_valid_new_hero():
    return {
        "name": fake.name(),
        "attack": fake.random_int(min=50, max=100),
        "defense": fake.random_int(min=50, max=100),
        "life": 500,
        "team": fake.random_int(min=0, max=1)
    }

def generate_invalid_new_hero():
    return {
        "name": fake.name(),
        "attack": fake.random_int(min=50, max=100),
        "defense": fake.random_int(min=50, max=100),
        "life": 500,
        "team": fake.random_int(min=2, max=3) # invalid field
    }

def battle(hero1, hero2):
    return requests.post(f"{ENDPOINT}/battle?hero1={hero1}&hero2={hero2}")

def invalid_battle(hero1, hero2):
    return requests.post(f"{ENDPOINT}/battle?hero={hero1}&hero2={hero2}") # wrong parameter name

def create_hero(payload):
    return requests.post(ENDPOINT, json=payload)

def update_hero(hero_id, payload):
    return requests.patch(ENDPOINT + f"/{hero_id}", json=payload)

def get_hero(hero_id):
    return requests.get(ENDPOINT + f"/{hero_id}")

def delete_hero(hero_id):
    return requests.delete(ENDPOINT + f"/{hero_id}")