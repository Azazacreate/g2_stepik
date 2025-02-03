''' #Теория
text = input('Введите текст: ')
print(text)

# как считывать числовые данные, введённые в одной строке ?
a, b, c = map(int, input().split())
print(a, b, c)

#
print (sum(map(int, input().split())))

#как считывать отдельные слова, которые записаны в одной строке через пробел ?
word_1, word_2, word_3 = input().split()
print(word_1, type(word_1))
print(word_2, type(word_2))
print(word_3, type(word_3))
'''


'''
# Практика
# Что увидим на экране после запуска следующего кода?
a, b, c = map(int, input().split())
print(a + b + c)


# Напишите программу, которая вычисляет среднее арифметическое четырех введенных целых чисел.
a, b, c, d = map(int, input().split())
print((a+b+c+d)/4)

# Напишите программу, которая находит наилучшую оценку ученика за решение пяти контрольных работ. 
a, b, c, d, e = map(int, input().split())
print(max(a, b, c, d, e))
'''


