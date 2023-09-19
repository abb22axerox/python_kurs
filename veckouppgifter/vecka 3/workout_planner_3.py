import os

workout_goals = ['Run 5 km', 'Lift 10 kg', 'Cycle 30 km']

def Clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def Print_message(message_type):
    Clear_terminal()

    if message_type == 'start':
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

    elif message_type == 'c':
        print('''.: THREE DAY PLANNER :.
-----------------------
    WORKOUT GOALS!    
  ONE DAY AT A TIME.  
-----------------------
0 | TODAY
1 | TOMORROW
2 | LATER
-----------------------''')

Print_message('start')

while True:
    if operation == 'n':
        workout_goals.remove(workout_goals[0])
        workout_goals.append('')
        Print_message('start')

    elif operation == 'c':
        Print_message('c')
        day_change = input('Change goal for day > ')

        if day_change == '0':
            workout_goals[0] = input('Goal for tomorrow > ')
            Print_message('start')

        elif day_change == '1':
            workout_goals[1] = input('Goal for tomorrow > ')
            Print_message('start')
            
        elif day_change == '2':
            workout_goals[2] = input('Goal for tomorrow > ')
            Print_message('start')

        else:
            print('''-----------------------
ERROR: Bad day
INFO:  Expected integer (0-2)
-----------------------''')
            input('Press enter to continue...')
            Print_message('start')

    elif operation == 'e':
        break

    else:
        print(f'''-----------------------
ERROR: Unknown operation ({operation})
-----------------------''')
        input('Press enter to continue...')
        Print_message('start')