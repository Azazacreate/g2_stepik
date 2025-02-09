'''
# найти все-делители_числа
# программа-1
# самая-простая находит все-делители_числа
n = int(input())
i = 1
while i <= n:
    if n % i == 0:
        print(i, end=' ')
    i += 1

# program-2
# алгоритмЛинейный эффективнее в-2-раза программы-1
n = int(input())
i = 1
while i <= n // 2:
    if n % i == 0:
        print(i, end=' ')
    i += 1
print(n)


# program-3: самая-эффективная
n = int(input())
i = 1
while i <= n ** 0.5:
    if n % i == 0:
        print(i, n // i)
    i += 1


# program-3.2 избавляемся от-корня
# вывести все-делители в-парах
n = int(input())
i = 1
while i * i <= n:
    if n % i == 0:
        if i == n // i:
            print(i)
        else:
            print(i, n // i)
    i += 1
'''


# program-3.3 добавим в-список
# n = int(input())
# i = 1
# a = []
# while i * i <= n:
#     if n % i == 0:
#         if i == n // i:
#             a.append(i)
#         else:
#             a.append(i)
#             a.append(n // i)
#     i += 1
# a.sort()
# print(a)


# program-3.4
n = int(input())
i = 1
a = []
while i * i <= n:
    if n % i == 0:
        a.append(i)
        if i != n // i:
            a.append(n // i)
    i += 1
a.sort()
print(sum(a))