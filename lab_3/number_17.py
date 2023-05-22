import random


p, s = 1, 0
A = [random.randint(10,100) for i in range(10)]

for a in A: s += a; p *= a
print('Сумма массива:', s)
print('Произведение массива:', p)

