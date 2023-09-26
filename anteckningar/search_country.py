countries = {

    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input('city > ')

 

# DIN LÖSNING NEDAN

city = city.title()

for country in countries:
    if city in countries[country]:
        print(country)
        break
else:
    print('FEL: Ingen matchning')