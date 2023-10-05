import os
import requests
import json
import time

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def list_cities(city):
    print(f'- {city.title()}')

def print_basic_message():
    clear_terminal()

    print('''.: JetSetPets :.
----------------''')

    cities = requests.get(api_url)
    cities = json.loads(cities.text)
    for city in cities['cities']:
        list_cities(city)

    print(16 * '-')

def pet_selection():
    print('''----------------
- bird
- cat
- dog
- fish
- mouse
- rabbit
----------------''')

while True:
    api_url = 'https://8fzqlwv0jd.execute-api.eu-north-1.amazonaws.com/'

    print_basic_message()

    city = (input('Select city > ')).lower()

    if city == 'stockholm':
        pet = input('Select pet: ')
        print(16 * '-')

        api_url += '/' + city
        r = requests.get(api_url)
        main_dict = json.loads(r.text)

        for person in main_dict['users']:

            person_api_url = api_url + '/' + person['id']
            r = requests.get(person_api_url)
            person_dict = json.loads(r.text)

            for animal in person_dict['animals']:
                if pet == animal['type']:
                    print(f"{person_dict['forename']} {person_dict['surname']} has a {animal['type']} named {animal['name']}")
        break


