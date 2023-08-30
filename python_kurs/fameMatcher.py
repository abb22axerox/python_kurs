fameArray = []
noMatch = True
printMatches = 'Match: '

class famousPeople:
    def __init__(self, name, gender, haircolor, eyecolor):
        self.name = name
        self.gender = gender
        self.haircolor = haircolor
        self.eyecolor = eyecolor

# required famous people
fameArray.append(famousPeople('Daniel Radcliffe', 'male', 'brown', 'brown'))
fameArray.append(famousPeople('Rupert Grint', 'male', 'red', 'blue'))
fameArray.append(famousPeople('Emma Watson', 'female', 'brown', 'brown'))
fameArray.append(famousPeople('Selena Gomez', 'female', 'brown', 'brown'))

# own famous people
fameArray.append(famousPeople('Rowan Atkinson', 'male', 'brown', 'brown'))
fameArray.append(famousPeople('Tom Cruise', 'male', 'brown', 'brown'))
fameArray.append(famousPeople('Barack Obama', 'male', 'brown', 'brown'))
fameArray.append(famousPeople('Donald Trump', 'male', 'blonde', 'brown'))
fameArray.append(famousPeople('Joe Biden', 'male', 'white', 'blue'))

print('''
.: FAME MATCHER :.
------------------
Search of the day!
female, brown, brown
------------------''')

searchedGender = input('Gender: ')
searchedHaircolor = input('Hair color: ')
searchedEyecolor = input('Eye color: ')

print('------------------')

for person in fameArray:
    if person.gender == searchedGender and searchedHaircolor == person.haircolor and searchedEyecolor == person.eyecolor:
        printMatches = printMatches + person.name + ', '
        noMatch = False

if noMatch == True:
    print('No match!')
else:
    print(printMatches[:-2])
