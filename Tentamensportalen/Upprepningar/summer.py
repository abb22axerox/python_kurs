result = 0

while True:
    try:
        number = int(input('> '))
    
    except ValueError:
        print('Not an integer')
        continue

    if number == 0:
        break
    else:
        result += number

print('--------------------')
print(f'RESULT: {result}')