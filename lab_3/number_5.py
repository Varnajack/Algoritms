a = input('Введите номер месяца от 1 до 12: ')
if a == "1" or a == "3" or a == "5" or a == "7" or a == "8" or a == "10" or a == "12":
    print('В этом месяце 31 день.')
elif a == "4" or a == "6" or a == "9" or a == "11":
    print('В этом месяце 30 дней.')
elif a == "2":
    answer = input('Год високосный? (да/нет): ')
    if answer.lower() == "да":
        print('В этом месяце 29 дней.')
    elif answer.lower() == "нет":
        print('В этом месяце 28 дней.')

    else:
        print('Неверный ввод данных!')