''' Теория
print(list(range(5)))   # [0, 1, 2, 3, 4]
print(list(range(0)))   # []
print(list(range(-10))) # []

print(list(range(100,10,-10)))  # последовательность:отрицательная

a, b, c = range(1, 4)
print(a, b)


v = iter(range(5))  # <range_iterator object>
next(v)             # 0
next(v)             # 1
v.__next__()        # 2
v.__next__()        # 3
print(next(v))      # 4
next(v)             # error StopIteration
'''

n = iter([43, True, 'string'])
print(next(n))
print(next(n))
print(next(n))


n = iter('string')
print(next(n))
print(next(n))
print(next(n))