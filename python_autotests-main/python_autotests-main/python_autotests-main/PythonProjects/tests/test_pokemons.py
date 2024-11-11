import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'dd818aadf032c184144d7908d3a0d4e9'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4971'
level = '5'



def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'level' : level})
    assert response.status_code == 200

