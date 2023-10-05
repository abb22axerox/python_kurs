import os
import json

database_path = 'python_kurs-1/veckouppgifter/vecka 5/notes.json'

f = open(database_path)
notes = json.loads(f.read())
f.close()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def print_list():
    for note in notes:
        print(f'- {note}')

def print_basic_message():
    clear_terminal()

    print('''.:  ALWAYSNOTE  :.
-- gold edition --
******************''')
    
    print_list()
    
    print('''------------------
view | view note
add  | add note
rm   | remove note
exit | exit program
------------------''')

print_basic_message()

while True:
    print_basic_message()

    selection = input('menu > ')
    print('------------------')

    if selection == 'view':
        title = input('title > ')
        no_match = True
        for note in notes:
            if title == note:
                print(f'''------------------
{notes[note]}
------------------''')
                no_match = False
                
        if no_match:
            print('''------------------
ERROR: Unknown note
------------------''')

    elif selection == 'add':
        title = input('title > ')
        descr = input('descr > ')
        notes[title] = descr
        print('''------------------
INFO: Note added
------------------''')
            
    elif selection == 'rm':
        title = input('title > ')
        try:
            del notes[title]
            print('''------------------
INFO: Note deleted
------------------''')
        except KeyError: #if you try to delete a key that does not exist
            print('''------------------
ERROR: Unknown note
------------------''')

    elif selection == 'exit':
        f = open(database_path, "w")
        f.write(json.dumps(notes))
        f.close()
        print(f'''INFO: Saved successfully to "{database_path}"
------------------''')
        break

    else:
        print(f'''ERROR: Unknown command ({selection})
------------------''')

    input('Press enter to continue...')