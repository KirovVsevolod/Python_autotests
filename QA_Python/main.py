import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0025d2303b8b50d57fbb319e3c7c5848'
HEADER = {'Content-Type': 'application/json',  'trainer_token': TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email" : "kirov.vsev@yandex.ru",
    "password" : "XDR$cft6"
}

body_confirmations={
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_name = {
    "pokemon_id": "271778",
    "name": "VVVSDF",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "271776"
}

#response=requests.post(url = f'{URL}/trainers/reg', headers=HEADER, json=body_registration)
#print(response.text)

#response_confirmations=requests.post(url = f'{URL}/trainers/confirm_email', headers=HEADER, json=body_confirmations)
#print(response_confirmations.text)


response_create=requests.post(url = f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.text) # Создание покемона

response_name=requests.put(url = f'{URL}/pokemons', headers=HEADER, json=body_name)
message = response_name.json()['message']
print(message) #Смена имени

response_pokeball=requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeball)
print(response_pokeball.text) #Поймал в покебол





