import os

notes = {'Important': 'Buy snow tires for my car', 
         'Notes from lecture': 'I may need to do some self study'}

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def list_notes():
    

def print_basic_message():
    clear_terminal()

    print('''.:  ALWAYSNOTE  :.
    -- gold edition --
    ******************
    - Important
    - Notes from lecture
    ------------------
    view | view note
    add  | add note
    rm   | remove note
    exit | exit program
    ------------------''')

def main_func():
    selection = input('menu > ')

    for k in notes:
        print(k)

    if selection == 'view':
        print('')

    elif selection == 'add':
        print(18 * '-')
        user_title = input('title > ')
        user_description = input('descr > ')

        notes[user_title] = user_description


    input('Press enter to continue...')
    main_func()
main_func()