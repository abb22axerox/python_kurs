f = open('database.csv')
csv = f.read()
f.close()

rows = csv.split('/n')
del rows[0]
del rows[-1]

print(rows)