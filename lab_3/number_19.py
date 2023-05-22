import random
from random import randint

def my_list(*args):
    lst = []
    for elem in args:
        if not isinstance(elem, list):
            lst.append(elem)
        else:
            lst.extend(my_list(*elem))
    return lst


len_mass = randint(10,10)
len_elem = randint(10,10)
a,b = 1,100
mass = [[random.randint(a,b) for _ in range(len_elem)] for _ in range(len_mass)]
print("Массив массивов:", mass)

print("Распакованный массив:", my_list(mass))