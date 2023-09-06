print('''--------------------
.: SUMMA SUMMARUM :.
--------------------
Stängs vid inmatning
 av negativt heltal 
--------------------''')

summa = 0
while True:
    i = input('Heltal: ')

    try:
        i = int(i)
        summa += 1
    except (ValueError, ZeroDivisionError):
        print('FEL: Ogiltigt heltal (' + i + ')')