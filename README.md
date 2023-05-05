# Python PyTest Suite for Marvel API

![Image](https://github.com/vmpires/vmpires/blob/main/marvel_pytest.jpeg)

#### Getting started

1) First, it's necessary to clone [Marvel API](https://github.com/vmpires/marvel_api) and Marvel PyTest

2) Install application requirements ([Poetry](https://python-poetry.org/) is needed)
        
        `poetry install`
        

3) Execute the command below on Marvel PyTest folder, passing the Marvel API path, where Dockerfile and docker-compose.yml are located
        
        `poetry run python -m marvel_e2e_pytest "<marvel_api_path>"`


4) Optionally is possible to create an `.env` file on the repository root and save API_PATH env with the Marvel API path like below

        `API_PATH=<marvel_api_path>`

5) Then run without having to pass it as an argument

        `poetry run python -m marvel_e2e_pytest`