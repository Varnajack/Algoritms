from random import randint

def selection_sort(my_list):
    for i in range(0, len(my_list) - 1):
        minimum = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[minimum]:
                minimum = j
        my_list[i], my_list[minimum] = my_list[minimum], my_list[i]

A = [randint(10,100) for i in range(10)]
print("Изначальный массив:", A)
A = [int(x) for x in A]
selection_sort(A)
print("Отсортированный массив:", A)