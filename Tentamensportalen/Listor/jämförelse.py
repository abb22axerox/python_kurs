list_a = [4, 1, 9, 4, 7, 9, 3, 8, 5, 8]
list_b = [4, 1, 1, 4, 7, 9, 6, 8, 5, 8]

# DIN LÖSNING NEDAN

for i in range(0, int(len(list_a))):
    if list_a[i] == list_b[i]:
        print(f'{i} <-> {list_b[i]}')
    
    else:
        print(f'{i} <-> {list_b[i]} <- DIFF!')
