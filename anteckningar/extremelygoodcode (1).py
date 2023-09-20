import subprocess

for i in range(1, 4):
   f = open('Bot_'+ str(i) + '.py' , 'w')
   f.write("import time\nimport random\nfor i in range(1,30):\n  f = open('Hallo_' + str(i) + str(random.randint(1,999)), 'w')\n  f.close() \n  time.sleep(1)")
   f.close()
   subprocess.run(['python', 'Bot_' + str(i) + '.py'])