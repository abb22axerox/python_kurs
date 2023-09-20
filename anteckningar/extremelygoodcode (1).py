# import subprocess
import os

def execute_python_file(file_path):
   os.system(f'python {file_path}')

for i in range(1, 11):
   f = open('Bot_'+ str(i) + '.py' , 'w')
   f.write("import time\nimport random\nfor i in range(1,10):\n  f = open('Hallo_' + str(i) + str(random.randint(1,999)), 'w')\n  f.write('Lol this is a virus!')\n  f.close()\n  time.sleep(0.01)")
   f.close()
   # subprocess.run(['python', 'Bot_' + str(i) + '.py'])
   execute_python_file('Bot_'+ str(i) + '.py')