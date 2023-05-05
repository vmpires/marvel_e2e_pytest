import requests

from marvel_e2e_pytest.tools.helpers import ENDPOINT

initial_value = None
end_value = None

def clean_db(initial_value, end_value):
    if not initial_value or not end_value:
        raise Exception("Initial or ending values not passed!")

    for i in range(initial_value, end_value):
        response = requests.delete(ENDPOINT + f"/{i}")
        if response.status_code == 200:
            print(response.status_code)
            print(response.json()['deleted']['id'])
        else:
            print(f"Hero {i} couldn't be deleted because: {response.json()}")

if __name__ == "__main__":
    clean_db(initial_value, end_value)