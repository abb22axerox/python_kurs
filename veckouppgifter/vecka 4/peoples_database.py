import os

f = open('database2.csv', 'r')
csv = f.read()
f.close()
rows = csv.split('\n')  # str -> list
del rows[0]
del rows[-1]

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_basic_message():
    clear_terminal()
    print('''.: PEOPLES DATABASE :.
----------------------
get_id | Get person by ID
scan_f | List people by FORENAME
scan_s | List people by SURNAME
exit | Exit program
----------------------''')

def print_results(columns):
    print(f'''ID:       {columns[0]}
FORENAME: {columns[1]}
SURNAME:  {columns[2]}
GENDER:   {columns[3]}
AGE:      {columns[4]}
----------------------''')
    
def main_func():
    print_basic_message()

    # reset variables
    user_id = 0
    user_forename = ''
    user_surname = ''
    no_match = True

    selection = input('| menu > ')

    valid_selections = ['get_id', 'scan_f', 'scan_s', 'exit']
    if selection not in valid_selections:
        print(22 * '-')
        print('ERROR: Unknown command')
        no_match = False
    elif selection == 'get_id':
        user_id = input('| ID = ')
    elif selection == 'scan_f':
        user_forename = input('| FORENAME = ')
    elif selection == 'scan_s':
        user_surname = input('| SURNAME = ')
    elif selection == 'exit':
        exit()
    print(22 * '-')

    for row in rows:
        columns = row.split(',')
        if columns[0] == user_id:
            print_results(columns)
            no_match = False
        elif columns[1].lower() == user_forename.lower():
            print_results(columns)
            no_match = False
        elif columns[2].lower() == user_surname.lower():
            print_results(columns)
            no_match = False
    
    if no_match == True:
        print('No match!')
        print(22 * '-')
    
    input('Press enter to continue...')
    main_func()
main_func()