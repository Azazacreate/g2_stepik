'''
a = [0, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 3, 2]
count = [0, 0, 0, 0, 0, 0]
for i in a:
    count[i] += 1
    print(i, count[i], count)


# посчитать сколько-раз встретился каждый-символ
string = 'abcdefghijklmnopqrstuvwxyz 5435134 (&*^%$@#%^ aaaaBB'
letters = [0] * 26
for i in string.lower():
    if i >= 'a' and i <= 'z':
        number = ord(i) - 97
        letters[number] += 1
for i in range(26):
    if letters[i] > 0:
        print(chr(i + 97), letters[i])


# program-3
import random
a = []
for i in range(10):
    a.append(random.randint(-10, 10))
count = [0] * 21
for i in a:
    count[i + 10] += 1
print(a)
for i in range(21):
    print(i-10, count[i])
'''

a = list(map(int, input()))
print(a)
count = [0] * 10
for i in a:
    count[i] += 1
for i in range(10):
    if count[i] > 0:
        print(i, count[i])
