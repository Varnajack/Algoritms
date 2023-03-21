count = 0
num_list = []
while count != 3:
    number = float(input('введите число: '))
    if number <= 5 and number >= 1:
        num_list.append(number)
    count += 1
print('Список чисел, входящих в интервал:', num_list)


