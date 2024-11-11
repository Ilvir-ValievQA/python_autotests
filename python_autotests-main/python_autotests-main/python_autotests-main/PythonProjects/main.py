import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'dd818aadf032c184144d7908d3a0d4e9'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "68033",
    "name": "mal",
    "photo_id": 2
}

body_pokebol = {
    "pokemon_id": "68033"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_pokebol = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokebol)
print(response_pokebol.text)