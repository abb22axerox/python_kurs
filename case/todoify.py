import os

todos = []

def Clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def Print_message(message_type):
    Clear_terminal()

    print('''****************************************
                Todoify
----------------------------------------
list   | List todos
add    | Add todo
check  | Check todo
delete | Delete todo
----------------------------------------
save   | Save todos in a file
load   | Load todos from file
----------------------------------------''')

    if message_type == 'start': 
        global operation
        operation = input('Selection > ')
    
    elif message_type == 'add':
        print(40 * '-')
        value = input('Todo description > ')
        todos.append(value)
        print('''
    SUCCESS: Todo added
''')
        input('Press enter to continue...')
        Print_message('start')

Print_message('start')

while True:
    if operation == 'list':
        Print_message('list')
    elif operation == 'add':
        Print_message('add')