"""
    Необходимо написать простой калькулятор,
    который оперирует с двумя числами и оператором.
    В зависимости от введенного оператора,
    между числами проводится определенная операция.
    Результат выводится на экран.
    * обработать все возможные ошибки программы с помощью try-except
"""
first_digit = input('Первое число: ')
try:
    first_digit = float(first_digit)
except ValueError:
    exit('Введено не число!')
operator = input('Оператор (*, /, -, +): ')
second_digit = input('Второе число: ')
try:
    second_digit = float(second_digit)
except ValueError:
    exit('Введено не число!')

result = None
if operator == '+':
    result = first_digit + second_digit
elif operator == '/':
    try:
        result = first_digit / second_digit
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')
elif operator == '*':
    result = first_digit * second_digit
elif operator == '-':
    result = first_digit - second_digit
else:
    print('Введен неверный оператор!')
print('Результат вычислений:', result)
