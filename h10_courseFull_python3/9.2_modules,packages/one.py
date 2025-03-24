# one.py
def function_1():
    print('function_1() in one.py')

print('уровеньВерхний внутри one.py')
if __name__ == '__main__':
    print('one.py запустилсяНапрямую')
else:
    print('one.py импортирован')


# 2
if __name__ == '__main__':
    function_1()