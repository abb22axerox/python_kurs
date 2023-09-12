import os

workout_goals = ['Run 5 km', 'Lift 10 kg', 'Cycle 30 km', '', '', '', '']

def Clear_terminal():
    os.system('cls')

def Print_basic_message(day_1, day_2, day_3):
    Clear_terminal()
    print(f'''.: THREE DAY PLANNER :.
-----------------------
    WORKOUT GOALS!    
ONE DAY AT A TIME.  
-----------------------
TODAY:    {workout_goals[day_1]}
TOMORROW: {workout_goals[day_2]}
LATER:    {workout_goals[day_3]}
-----------------------
n | Next day
c | Change goal
e | Exit program
-----------------------''')
    global operation
    operation = input('operation > ')

def Print_change_message():
    Clear_terminal()
    print('''.: THREE DAY PLANNER :.
-----------------------
    WORKOUT GOALS!    
  ONE DAY AT A TIME.  
-----------------------
0 | TODAY
1 | TOMORROW
2 | LATER
-----------------------''')

# startup code
day_1 = 0
day_2 = 1
day_3 = 2
Print_basic_message(day_1, day_2, day_3)

while True:
    if operation == 'n':
        day_1 += 1
        day_2 += 1
        day_3 += 1
        Print_basic_message((day_1),(day_2),(day_3))

    elif operation == 'c':
        Print_change_message()
        day_change = input('Change goal for day > ')
        if day_change == '0':
            workout_goals[day_1] = input('Goal for tomorrow > ')
            Print_basic_message(day_1, day_2, day_3)
        elif day_change == '1':
            workout_goals[day_2] = input('Goal for tomorrow > ')
            Print_basic_message(day_1, day_2, day_3)
        elif day_change == '2':
            workout_goals[day_3] = input('Goal for tomorrow > ')
            Print_basic_message(day_1, day_2, day_3)

    elif operation == 'e':
        break
exit()