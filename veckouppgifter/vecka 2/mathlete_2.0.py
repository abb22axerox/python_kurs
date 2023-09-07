print('''.: MATHLETE v2.0 :.
-------------------''')

exit = False
cardinality = 0
user_input = ''
sum = 0

while exit == False:
    user_input = input('> ')
    if user_input != 'exit':
        try:
            sum += int(user_input)
            cardinality += 1
        except ValueError:
            print('ERROR: Invalid number')
    else:
        exit = True

try:
    print(f'''-------------------
Cardinality: {cardinality}
Sum:         {sum}
Mean value:  {(sum/cardinality)}''')

except ZeroDivisionError:
    print(f'''-------------------
Cardinality: {cardinality}
Sum:         {sum}
Mean value:  NaN''')