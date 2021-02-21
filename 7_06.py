"""
    Задание 7.06
    Создать функцию, которая принимает на вход
    неопределенное количество аргументов и
    возвращает их сумму и максимальное из них.
"""
def sum_elements(*args):
    sum = 0
    maxx = args[0]
    for i in args:
        sum += int(i)
        if int(i) > maxx:
            maxx = i

    return f'sum_of_elements = {sum} \nmax_element = {maxx}'

s_list = input('Input arguments (use space): ')
list_arguments = list(map(int,s_list.split()))
print(sum_elements(*list_arguments))














