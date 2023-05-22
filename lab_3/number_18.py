from random import randint

def my_list(*args):
    lst = []
    for elem in args:
        if not isinstance(elem, list):
            lst.append(elem)
        else:
            lst.extend(my_list(*elem))
    return lst

a,b = 1,100
mass = [[randint(a,b) for _ in range(randint(10,10))] for _ in range(randint(10,10))]
print("Массив массивов:", mass)

print("Распакованный массив:", my_list(mass))

p, s = 1, 0
for a in my_list(mass): s += a; p *= a

print('Сумма массива:', s)
print('Произведение массива:', p)
