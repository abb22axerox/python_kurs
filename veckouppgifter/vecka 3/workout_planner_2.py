import os

workout_goals = ['Run 5 km', 'Lift 10 kg', 'Cycle 30 km']

def Clear_terminal():
    os.system('cls')

def Print_basic_message():
    Clear_terminal()
    print(f'''.: THREE DAY PLANNER :.
-----------------------
    WORKOUT GOALS!    
  ONE DAY AT A TIME.  
-----------------------
TODAY:    {workout_goals[0]}
TOMORROW: {workout_goals[1]}
LATER:    {workout_goals[2]}
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
Print_basic_message()

while True:
    if operation == 'n':
        workout_goals.remove(workout_goals[0])
        workout_goals.append('')
        Print_basic_message()

    elif operation == 'c':
        Print_change_message()
        day_change = input('Change goal for day > ')
        if day_change == '0':
            workout_goals[0] = input('Goal for tomorrow > ')
            Print_basic_message()
        elif day_change == '1':
            workout_goals[1] = input('Goal for tomorrow > ')
            Print_basic_message()
        elif day_change == '2':
            workout_goals[2] = input('Goal for tomorrow > ')
            Print_basic_message()

    elif operation == 'e':
        break