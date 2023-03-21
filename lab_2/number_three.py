count = 0
num_list = []
while count != 3:
    number = float(input('введите число: '))
    if number > 0:
        number **= 2
        num_list.append(number)
    count += 1
print('Список квадратов чисел, которые больше нуля:', num_list)