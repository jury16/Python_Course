"""
    Задание 5.05
    Создать список с фамилиями. Вывести все фамилии,
    которые начинаются на П и заканчиваются на а
"""
s = input('Input las name (for stop input "0"): ')
a = []
if not len(s):
    print('end')
else:
    while s != "0":
        a.append(s)
        s = input('Input las name (for stop input "0"): ')
    for i in a:
        if i[0] == 'П' and i[-1] == 'а':
            print(i)
