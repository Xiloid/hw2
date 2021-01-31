"""
    Вводится число от 1 до 999
    (если введено не число либо число вне диапазона - вывести сообщение)
    1. Найти сумму цифр числа.
    2. Вывести на экран, порядок, в котором расположены цифры числа
        (возростание/убывание/в разброс(равны))
"""
try:
    num = int(input('Число от 1 до 999: '))
except ValueError:
    exit('Введено НЕ число!')
result = units = dozens = hundreds = 0
if 0 < num < 1000:
    units = num % 10
    if 9 < num < 100:
        dozens = num // 10
        if units > dozens:
            print('Числа по возрастанию')
        elif units < dozens:
            print('Числа по убыванию')
        else:
            print('Числа равны')
        result = units + dozens
        print('Сумма всех чисел:', result)
    elif 99 < num < 1000:
        dozens = num % 100 // 10
        hundreds = num // 100
        if units < dozens < hundreds or units == dozens < hundreds or units < dozens == hundreds:
            print('Числа по убыванию')
        elif hundreds < dozens < units or units == dozens > hundreds or units > dozens == hundreds:
            print('Числа по возрастанию')
        elif units == dozens and dozens == hundreds:
            print('Числа равны')
        else:
            print('Числа в разнобой')
        result = units + dozens + hundreds
        print('Сумма всех чисел:', result)
    else:
        result = units
        print('Сумма числа равна числу:', result)
else:
    print('Число вне диапазона!')
