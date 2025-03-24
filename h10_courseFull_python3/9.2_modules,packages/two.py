# two.py
import one
print('уровеньВерхний внутри two.py')
one.function_1()

if __name__ == '__main__':
    print('two.py запустилсяНапрямую')
else:
    print('two.py импортирован')