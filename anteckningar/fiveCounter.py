print('''-----------------
.: FIVECOUNTER :.
-----------------
Programmet stängs
när ett negativt
heltal matas in.
-----------------''')

fives = 0
i = 0

while 0 <= i:
    i = int(input('Heltal: '))
    if i == 5:
        fives += 1
    

print(f'''-----------------
      ANTAL FEMMOR: {fives}''')