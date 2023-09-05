import random
import math

print('''.: THE HIGHER LOWER GAME :.
---------------------------
Welcome to The Higher Lower
Game. I  will  randomise  a
number between  0  and  99.
Can you guess it?
---------------------------''')

guessed_Number = input('Your guess > ')

random_Number = math.ceil((random.random())*100)

print(random_Number)

while guessed_Number < random_Number:
    print('LOWER!')
    guessed_Number = input('Try again > ')

while guessed_Number > random_Number:
    print('HIGHER!')
    guessed_Number = input('Try again > ')

if guessed_Number == random_Number:
    print('rätt')