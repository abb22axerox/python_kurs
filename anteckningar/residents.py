import json

with open('python_kurs-1/anteckningar/people.json') as f:
    people = f.read()
    people = json.loads(people)

with open('python_kurs-1/anteckningar/residents.json') as f:
    residents = f.read()
    residents = json.loads(residents)

print('''.: Resident Lookup :. 
---------------------''')

name = input('Slå upp namn > ')
print('---------------------')

for person in people:
    if name == person['name']:
        resident_id = person['resident']
        break

for resident in residents:
    if resident_id == resident['id']:
        print('BOSTAD:', resident['type'])
        print('HYRA:', resident['rent'])

for person in people:
    if resident_id == person['resident']:
        print('-', person['name'])