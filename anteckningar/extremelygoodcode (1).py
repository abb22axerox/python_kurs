import subprocess

for i in range(1, 3):
   f = open('Bot_'+ str(i) + '.py' , 'w')
   f.write("import time \nimport random \nimport subprocess \nfor i in range(1,3): \n f = open('Hallo_' + str(i) + str(random.randint(1,999)), 'w') \n f.close() \n time.sleep(0.1) \nsubprocess.run(['python', 'Bot_2.py'])")
   f.close()

subprocess.run(['python', 'Bot_1.py'])