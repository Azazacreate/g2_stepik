'''
for i in range(3):
    for j in range(5):
        print('*', end='')
    print()

for i in range(3):
    for j in range(5):
        print(i, end='')
    print()

for i in range(3):
    for j in range(5):
        print(j, end='')
    print()


# длина пароля = 3
from string import printable
print(len(printable))
for b1 in printable:
    for b2 in printable:
        for b3 in printable:
            print(b1, b2, b3)
# 100^3 = 1_000_000-паролей


# table-multiply
a = []
for i in range(1, 11):
    for j in range(1,11):
        a.append(i * j)
    print(a)
    a = []


# задача из-ЕГЭ (комбинаторика)
# Сколько слов из-6-букв, которые начинаются и заканчиваются буквой:согласной
# и содержат только-2-гласные можно
k = 0
for b1 in 'тыква':
    for b2 in 'тыква':
        for b3 in 'тыква':
            for b4 in 'тыква':
                for b5 in 'тыква':
                    for b6 in 'тыква':
                        words = b1 + b2 + b3 + b4 + b5 + b6
                        if words[0] in 'ткв' and words[-1] in 'ткв':
                            if words.count('ы') + words.count('а') == 2:
                                # print(words)
                                k += 1
print('количество-слов =', k)


x = int(input())
sum = 0
while x > 0:
    sum += x % 10
    x //= 10
print(sum)
'''


for i in range(1, 101):
    x = i
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    print(i, sum)


# используют циклыВложенные, чтобы перебрать элементы_списковВложенных
