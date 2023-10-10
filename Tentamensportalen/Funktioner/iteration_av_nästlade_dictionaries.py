
def print_all_keys(dictionary):
    for key in dictionary:
        value = dictionary[key]
        print(key)

        if type(value) == dict:
            print_all_keys(value)

# DIN KOD OVAN
person = {
    'namn': 'Petra Svensson',
    'bostad': {
        'typ': 'hyra',
        'avgift': 5000
    },
    'husdjur': {
        'Douglas': {
            'typ': 'hund'
        },
        'Stampe': {
            'typ': 'kanin'
        }
    }
}

print_all_keys(person)
 