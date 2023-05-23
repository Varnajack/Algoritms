def anagramCheck(str1, str2):

    list1 = list(str1)
    list2 = list(str2)

    list1.sort()
    list2.sort()

    position = 0
    matches = True

    if len(list1) != len(list2):
        matches = False
        return matches

    while position < len(str1) and matches:
        if list1[position] == list2[position]:
            position = position + 1
        else:
            matches = False

    return matches

firstword = 'python'
secondword = 'pnohty'
print('Первая последовательность:', firstword)
print('Вторая последовательность:', secondword)
print('Это анограммы' if anagramCheck(firstword, secondword) else 'Это не анограммы')