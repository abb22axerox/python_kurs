import random

print('''.: THE HIGHER LOWER GAME :.
---------------------------
Welcome to The Higher Lower
Game. I  will  randomise  a
number between  0  and  99.
Can you guess it?
---------------------------''')
      
random_Number = random.randint(1, 99)
guessed_Number = int(input('Your guess > '))
guesses = 0

while guessed_Number != random_Number:
    if guessed_Number > random_Number:
        print('LOWER!')
        guessed_Number = int(input('Try again > '))
        guesses += 1
    elif guessed_Number < random_Number:
        print('HIGHER!')
        guessed_Number = int(input('Try again > '))
        guesses += 1

print(f'''---------------------------
{guessed_Number} is correct!
It took you {guesses} guesses.
Good job!''')