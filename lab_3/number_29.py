def list_separation(my_list):
    string = ''
    for elem in my_list:
        string += elem + " "
    return string

my_list = ['Привет','мир']

print('Массив строк:', my_list)
print('Преобразованная строка:', list_separation(my_list))