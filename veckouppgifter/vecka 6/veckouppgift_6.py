import os
import requests
import json

api_url = 'https://8fzqlwv0jd.execute-api.eu-north-1.amazonaws.com/'

cities = requests.get(api_url)
cities = json.loads(cities.text)

# list cities function
def list_cities(city):
    print(f'- {city.title()}')

# clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

print('''.: JetSetPets :.
----------------''')

# list cities from api
for city in cities['cities']:
    list_cities(city)
print(16 * '-')

city = (input('Select city > ')).lower()

if city not in cities['cities']:
    print('''----------------
ERROR: City not found''')
    exit()

print('''----------------
- bird
- cat
- dog
- fish
- mouse
- rabbit
----------------''')

pet = (input('Select pet: ')).lower()
print(16 * '-')

valid_pets = ['bird', 'cat', 'dog', 'fish', 'mouse', 'rabbit']

if pet not in valid_pets:
    print('ERROR: Pet not found')
    exit()

# get city url dictionary
city_url = api_url + city
r = requests.get(city_url)
main_dict = json.loads(r.text)

for person in main_dict['users']:
    # person url dictionary
    person_url = city_url + '/' + person['id']
    r = requests.get(person_url)
    person_dict = json.loads(r.text)

    # loop animal list
    for animal in person_dict['animals']:
        # check if the type is correct
        if pet == animal['type']:
            # print results
            print(f"{person_dict['forename']} {person_dict['surname']} has a {animal['type']} named {animal['name']}")