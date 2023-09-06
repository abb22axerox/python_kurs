import random
import time

player_score = 0
dealer_score = 0

print('You')
print(str(player_score))
input()
dice = random.randint(1,6)
player_score += dice
print('')

time.sleep(1)