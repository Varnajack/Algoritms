from random import randint

A = [randint(10,100) for i in range(10)]

even_count, odd_count = 0, 0

# iterating each number in list
for num in A:

    # checking condition
    if num % 2 != 0:
        odd_count += 1

print("Массив:", A)

print("ол-во нечетных чисел в массиве: ", odd_count)