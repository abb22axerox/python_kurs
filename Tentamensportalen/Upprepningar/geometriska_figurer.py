shape = input('shape: ')
height = int(input('height: '))

# DIN KOD NEDAN

if shape == 'triangle':
    for i in range(1, (height + 1)):
        print(i * '#')

elif shape == 'rectangle':
    width = int(input('width: '))
    for i in range(1, (height + 1)):
        print(width * '#')

elif shape == 'square':
    for i in range(1, (height + 1)):
        print(height * '#')