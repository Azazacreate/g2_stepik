# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Создание простого DataFrame
# data = {
#     'Год': [2020, 2021, 2022, 2023],
#     'Продажи': [150, 200, 250, 300]
# }
#
# df = pd.DataFrame(data)
#
# # Визуализация данных
# plt.figure(figsize=(10, 5))
# plt.plot(df['Год'], df['Продажи'], marker='o')
# plt.title('Продажи по годам')
# plt.xlabel('Год')
# plt.ylabel('Продажи')
# plt.grid()
# plt.xticks(df['Год'])  # Устанавливаем метки по оси X
# plt.show()


# try:
#     import numpy
#     import pandas
#     import matplotlib
#     import jupyter
#     import seaborn
#     import nltk
#     import tensorflow
#     # import scikit_learn
#     import keras
#
#     # import torch
#
#     print("Все библиотеки установлены!")
# except ImportError as e:
#     print(f"Ошибка: {e.name} не установлена.")

'''
1. numpy: Библиотека для работы с многомерными массивами и матрицами, а также для выполнения математических операций.
2. pandas: Библиотека для работы с данными, которая предоставляет удобные структуры данных и инструменты для анализа.
3. matplotlib: Библиотека для визуализации данных.
4. seaborn: Библиотека для визуализации данных, основанная на matplotlib, которая предоставляет более высокоуровневый интерфейс.
5. scikit-learn: Библиотека для машинного обучения, которая включает в себя множество алгоритмов и инструментов для обработки данных.
6. tensorflow: Библиотека для глубокого обучения, разработанная Google.
7. keras: Высокоуровневый API для глубокого обучения, который может использоваться с TensorFlow.
8. pytorch: Библиотека для глубокого обучения, разработанная Facebook, известная своей гибкостью и простотой использования.
9. jupyter: Инструмент для создания интерактивных записных книжек, который позволяет вам комбинировать код, визуализации и текст.
'''


# отладка
# a = [3, 2, 3, 4, 5, 6, 7, 3, 3, -70]
# while 3 in a:
#     a.remove(3)
#     print(a)


# lowercase
a = input().split()
b = []
for el in a:
    a2 = el.lower()
    if a2 not in [el2.lower() for el2 in b]:
        b.append(el)
print(*b)