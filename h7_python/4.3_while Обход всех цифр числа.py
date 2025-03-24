''' 4.3 Обход всех цифр числа с помощью while
x = 4768
while x>0 :
    print(x % 10)
    x = x // 10
    # не-перепутайте порядок_операций

# получить всю-информацию о-числе
x = int(input('input your number: '))
count_digits = 0
count_even = 0
count_odd = 0
sum = 0
pr = 1
min = int(str(x)[0])
max = int(str(x)[0])
while x > 0:
    numberLast = x % 10
    count_digits += 1
    if numberLast % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    sum += numberLast
    pr *= numberLast
    if numberLast < min:
        min = numberLast
    if numberLast > max:
        max = numberLast
    x = x // 10
print('count_digits = ', count_digits)
print('count_even = ', count_even)
print('count_odd = ', count_odd)
print('sum = ', sum)
print('pr = ', pr)
print('min = ', min)
print('max = ', max)
'''


# записьДвоичная
# x = 14
# while x > 0:
#     print(x % 2)
#     x = x // 2


# Practice
# x = int(input())
# while x > 0:
#     print(x % 2)
#     x = x // 2