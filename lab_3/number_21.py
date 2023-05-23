from random import randint

A = [randint(1,10) for i in range(5)]

# printing original list
print("Массив:", A)

# using naive method to
# check sorted list
flag = 0
i = 1
while i < len(A):
    if (A[i] < A[i - 1]):
        flag = 1
    i += 1

# printing result
if (not flag):
    print("Да, массив отсортирован.")
else:
    print("Нет, массив не отсортирован.")