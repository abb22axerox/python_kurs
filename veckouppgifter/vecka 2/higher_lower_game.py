import random

print('''.: THE HIGHER LOWER GAME :.
---------------------------
Welcome to The Higher Lower
Game. I  will  randomise  a
number between  0  and  99.
Can you guess it?
---------------------------''')
      
random_number = random.randint(1, 99)
guessed_number = int(input('Your guess > '))
guesses = 1

while guessed_number != random_number:
    if guessed_number > random_number:
        print('LOWER!')
        guessed_number = int(input('Try again > '))
        guesses += 1
    elif guessed_number < random_number:
        print('HIGHER!')
        guessed_number = int(input('Try again > '))
        guesses += 1

print(f'''---------------------------
{guessed_number} is correct!
It took you {guesses} guesses.
Good job!''')