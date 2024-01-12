iteration = 0
value = 0

while True:
    number = input('> ')
    iteration += 1
    if number == 'exit':
        iteration -= 1
        break
    else:
        value += int(number)

print('---------------')
print(f'{(value/iteration)}')