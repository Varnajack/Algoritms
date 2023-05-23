from random import randint

A = [randint(10,100) for i in range(10)]

print("Массив:", A)

minimum = min(A)
position = [i for i, j in enumerate(A) if j == minimum]

print("Номер(а) наименьшего элемента в массиве:", position)