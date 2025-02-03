'''
# Алгоритм Евклида
# программа-1
# найти НОД 2-чисел
# НОД(12, 6) = 6
a = int(input())
b = int(input())
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(b)
'''


# программа-3
# a = int(input())
# b = int(input())
# while b > 0:
#     c = a % b
#     a = b
#     b = c
# print(a)


# программа-3.2
a = int(input())
b = int(input())
while b > 0:
    a, b = b, a % b
print(a)