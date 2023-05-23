def list_generation(string):
    string += ' '
    word = ''
    my_list = list()
    for elem in string:
        if elem == ' ':
            my_list.append(word)
            word = ''
        else:
            word += elem
    return my_list

string = 'Привет мир'

print('Строка:', string)
print('Массив строк:', list_generation(string))