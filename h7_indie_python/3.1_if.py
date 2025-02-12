'''task-1
На вход программе поступает одно слово.
Если это строка «Python», программа выводит ДА, в противном случае программа выводит НЕТ'''
# if input() == 'Python':
#  print('ДА')
# else:
#  print('НЕТ')


'''task-2
Заплатите налоги
Во всех странах присутствует подоходный налог. В каких-то странах он больше, в каких-то меньше. В РФ граждане платят подоходный налог в размере 13%.
Представьте теперь, что люди с доходом меньше 20000 рублей освобождены от уплаты налога. Напишите программу, которая получает на вход значение дохода в виде целого числа и выводит на экран сумму, оставшуюся после уплаты налога в 13%. Если у человека зарплата меньше 20000р налог не удерживается.'''
 # a = int(input())
 # if a >= 20000:
 #     print(a * 0.87)
 # else:
 #     print(a)


'''task-3
Вводятся два целых числа, каждое в отдельной строке.
Ваша задача вывести наибольшее из данных чисел.
Примечание: используйте только условный оператор, функцией max пользоваться нельзя'''
 # a = int(input())
 # b = int(input())
 # print(*[a if a >= b else b])


'''task-4
Программа получает на вход три натуральных числа A, B и C через пробел. 
Вам необходимо вывести YES в том случае, если A + B = C и вывести NO в противном случае.
'''
 # a = list(map(int, input().split()))
 # print('YES' if (a[0] + a[1]) == a[2] else 'NO')


'''task-5
Метод remove
Программа получает на вход список из целых чисел, при этом гарантируется, что числа в списке повторяться не будут.
Ваша задача удалить из этого списка числа 3, 5, 7 и 9. 
Обратите внимание, что каждое из чисел 3, 5, 7 и 9. необязательно должно присутствовать в введенном списке.
В качестве ответа необходимо распечатать измененный список
* Примечание: Чтобы прочитать из ввода целые числа и сохранить их в виде списка в переменной a вам необходимо написать строчку
a = list(map(int, input().split()))'''
 # list_1 = list(map(int, input().split()))
 # if 3 in list_1:
 #     list_1.remove(3)
 # if 5 in list_1:
 #     list_1.remove(5)
 # if 7 in list_1:
 #     list_1.remove(7)
 # if 9 in list_1:
 #     list_1.remove(9)
 # print(list_1)


'''task-5.2'''
 # a = list(map(int, input().split()))
 # [a.remove(i) for i in (3, 5, 7, 9) if i in a]
 # print(a)


''' Моржовый оператор'''


'''task-6
Таможня
На момент написания текста из РФ можно было вывозить не более 10000$ или эквивалент в другой валюте. При превышении этой суммы необходимо составлять декларацию.

Давайте представим, что сумму выше 10000 долларов таможня забирает себе и вам останется только 10000$.

Давайте напишем такую программу, которая будет принимать целое положительное число - сумма в долларах. Если она не превышает 10000$, то выводим текст Сумма <значение> не превышает лимит, проходите

Если сумма превышает 10000$ выводим текст Ого! <значение>! Куда вам столько? Мы заберем <разница>

И конечно же нужно использовать сами знаете кого, иначе ваше решение не пройдет
* моржовый оператор
'''
# if (a := int(input())) <= 10000:
#     print(f'Сумма {a} не превышает лимит, проходите')
# else:
#     print(f'Ого! {a}! Куда вам столько? Мы заберем {a-10000}')


'''task-7
Еще одна моржовая тренировка
На вход вашей программе поступает фраза, если в ней присутствует слово walrus выводим текст Нашли моржа, иначе выводим Никаких моржей тут нет.
* И конечно же нужно использовать сами знаете кого, иначе ваше решение не пройдет
* Следующие задачи можете решать без моржового оператора
'''
# print('Нашли моржа' if 'walrus' in (a := input()) else 'Никаких моржей тут нет')


'''task-8
Программа принимает на вход два слова s и t. 
Если слово t является словом s, записанным наоборот, выведите YES, иначе выведите NO.
Слова состоят из маленьких латинских букв. Входные данные не содержат лишних пробелов. Слова непустые, и их длины не превосходят 100 символов.'''
# s, t = input(), input()
# print('YES' if s == t[::-1] else 'NO')


'''task-9
Требуется написать программу, определяющую, является ли четырехзначное натуральное число N палиндромом, т.е. числом, которое одинаково читается слева направо и справа налево.
Программа получает на вход целое положительное четырехзначное число N  и должна вывести YES,  если число N является палиндромом, и NO - если не палиндром.
'''
# N = input()
# print('YES' if N == N[::-1] else 'NO')


'''task-10
Даны три натуральных числа a, b, c записанные в отдельных строках. Ваша задача определить, существует ли треугольник с такими сторонами. 

Для этого вспоминаем теорему о существовании треугольника. Она утверждает, что треугольник существует, если сумма любых двух сторон больше оставшейся третьей.
Выведите строку YES, если условие теоремы выполняется, иначе выведите строку NO.
'''
# a, b, c = int(input()), int(input()), int(input())
# print('YES' if (a + b > c and a + c > b and b + c > a) else 'NO')


'''task-11
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером (иногда и с незначащими нулями), где сумма первых трех цифр равна сумме последних трех. Т.е. билеты с номерами 385916 и 2011 – счастливые, т.к. 3+8+5=9+1+6 и 0+0+2=0+1+1. Вам требуется написать программу, которая проверяет «счастливость» билета.

Программа получает на вход одно целое число N (0 ≤ N < 106) и должна вывести «YES», если билет с номером N счастливый и «NO» в противном случае.

385916 -> YES
123344 -> YES
5203 -> YES     (005203 -> YES)
'''
# a = input()
# while len(a) < 6:
#     a = '0' + a
# if int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) + int(a[5]):
#     print('YES')
# else:
#     print('NO')


'''task-12
Напишите программу, которая на вход получает координаты двух клеток шахматной доски и выводит сообщение о том, являются ли эти клетки одного цвета. 
*Столбцы на шахматной доске обозначаются английскими строчными буквами.

Программа должна выводить YES, когда клетки одного цвета, NO - разного. Гарантируется, что значение колонок это латинские буквы abcdefgh, а строки это символы цифр от 1-8
'''


def are_cells_same_color(cell1, cell2):
    # Определяем координаты клеток
    column1, row1 = cell1[0], int(cell1[1])
    column2, row2 = cell2[0], int(cell2[1])
    # Преобразуем буквы столбцов в числа
    column1_index = ord(column1) - ord('a')
    column2_index = ord(column2) - ord('a')
    # Определяем цвета клеток
    color1 = (column1_index + row1) % 2
    color2 = (column2_index + row2) % 2
    # Сравниваем цвета клеток
    if color1 == color2:
        return "YES"
    else:
        return "NO"
# Ввод координат клеток
cell1 = input("Введите координаты первой клетки (например, a1): ")
cell2 = input("Введите координаты второй клетки (например, h8): ")

# Вывод результата
print(are_cells_same_color(cell1, cell2))
