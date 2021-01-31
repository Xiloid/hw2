"""
    Программа принимает на ввод координаты точки - x и y.
    Выводит, в какой четверти системы координат лежит точка.
                ^ y
                |
            II  |    I
                |
        --------=-------->
                |         x
            III |    IV
                |
"""
try:
    x = float(input('Введите X: '))
    y = float(input('Введите Y: '))
except ValueError:
    exit('Введено НЕ число!')
try:
    y = int(y)
except ValueError:
    exit('Введено НЕ число!')
if x > 0 and y > 0:
    print('I-я четверть')
elif x < 0 and y > 0:
    print('II-я черверть')
elif x < 0 and y < 0:
    print('III-я черверть')
elif x > 0 and y < 0:
    print('IV-я четверть')
else:
    print('Точка в нулевой координате!')
