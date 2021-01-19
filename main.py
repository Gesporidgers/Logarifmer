import math
print('Вас приветствует логарифмер.')
print('Выберите тип (1 - Двоичный, 2 - Стандартный десятичный)')
a = int(input())
b = float(input('Введите число: '))
if a == 1 :
    print(math.log(b, 2))
elif a == 2 :
    print(math.log(b))
else:
    print('Ошибка!')
