import random

print('''HIGHER LOWER
---------''')

random_number = random.randint(0, 99)

guess = int(input('> '))

guesses = 0

while True:
    if guess == random_number:
        break
    elif guess < random_number:
        print('HIGHER!')
    else:
        print('LOWER!')
    guess = int(input('Try again > '))
    guesses += 1

print('Right!')