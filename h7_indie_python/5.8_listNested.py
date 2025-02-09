'''
# список:2-мерный
listNested = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(listNested, end='\n\n')


# список:3-мерный
width = 3
height = 3
depth = 3
list_3 = [[[0 for z in range(depth)] for y in range(height)] for x in range(width)]
list_3[1][1][1] = 1     # ставим "1" в центре куба
a = []
b = []
for x in range(width):
    for y in range(height):
        for z in range(depth):
            a.append(list_3[x][y][z])
        b.append(a)
        a = []
    print(b)
    b = []
'''

a = []
for i in range(6):
    for j in range(7):
        a.append([i][j])
    print(a)