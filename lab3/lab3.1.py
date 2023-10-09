stroka = input('Введите строку: ')
stroka_list = list(stroka)
duplicate = []
for i in stroka_list:
    if stroka_list.count(i) > 1 and i not in duplicate:
        duplicate.append(i)
        numbers = stroka_list.count(i)
        duplicate.append(numbers)
    elif stroka_list.count(i) == 1:
        duplicate.append(i)
print(''.join(map(str, duplicate)))