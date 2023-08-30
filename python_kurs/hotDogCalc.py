import math

print("""
.: HOT DOG PLANNER :.
---------------------
How many students wants...""")

studentsMeat_2 = int(input("2 hot dogs (meat) > "))
studentsMeat_3 = int(input("3 hot dogs (meat) > "))
studentsVegan_2 = int(input("2 vegan hot dogs  > "))
studentsVegan_3 = int(input("3 vegan hot dogs  > "))

packagesHotDogsMeat = math.ceil((studentsMeat_2 * 2 + studentsMeat_3 * 3)/8)
packagesHotDogsVegan = math.ceil((studentsVegan_2 * 2 + studentsVegan_3 * 3)/4)
totalStudents = studentsMeat_2 + studentsMeat_3 + studentsVegan_2 + studentsVegan_3

totalPrice = packagesHotDogsMeat * 20.95 + packagesHotDogsVegan * 34.95 + totalStudents * 13.95

print(f"""---------------------
| Meat:   {packagesHotDogsMeat} packages
| Vegan:  {packagesHotDogsVegan} packages
| Drinks: {totalStudents} drinks
---------------------
| {totalPrice} SEK
---------------------""")