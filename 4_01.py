
"""
    Задания 3.11
    Ввести почтовый адрес. Проверить доменной имя. В случае если оно
    gmail.com, вывести на экран имя почтового ящика. Иначе вывести надпись
    “DOMAIN NAME is not supported’
"""
a = input('Input lust of numbers:   ')
list_a = a.split()
sum = 0
for i in list_a:
    if int(i) > 10:
        sum += int(i)
print(sum)






