"""
    Задание 7.06
    Создать функцию, которая принимает на вход
    неопределенное количество аргументов и
    возвращает их сумму и максимальное из них.
"""
def sum_elements(*args):
    sum = 0
    maxx = int(args[0][0])
    for i in (args[0]):
        sum += int(i)
        if int(i) > maxx:
            maxx = i

    return sum, int(maxx)

s_list = input('Input arguments (use space): ')
list_arguments = tuple(s_list.split())
print(sum_elements(list_arguments))














