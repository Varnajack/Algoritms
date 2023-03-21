import math

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

gem_abs = math.pow(a * b *c, 1./3)
print('Дробная часть равна:', gem_abs % 1)