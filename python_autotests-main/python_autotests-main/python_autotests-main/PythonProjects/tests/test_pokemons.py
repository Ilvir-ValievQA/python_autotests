import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f1a2424a8940277b4de760c1e2973b9d'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '8785'
level = '5'



def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'level' : level})
    assert response.status_code == 200

