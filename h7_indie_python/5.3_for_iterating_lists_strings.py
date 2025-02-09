'''
a = [1, 2, 3, 4, 5, 5]
for i in a:
    print(i, a.index(i))


a = [1, 2, 3, 4, 5, 5]
for i in range(len(a)):
    print(i, a[i])


# убираем дубли без-set()
a = [1, 2, 3, 4, 5, 5]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)
'''


s = 'string_number#1'
for i in s:
    print(i)