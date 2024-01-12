big_number = 0

while True:
    try:
        number = int(input('> '))
    
    except ValueError:
        print('Not an integer')
        continue

    if number == 0:
        break

    if big_number < number:
        big_number = number

print('--------------------')
print(f'RESULT: {big_number}')