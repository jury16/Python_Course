"""
    ЗЗадание 7.05
    Создать функцию, принимающая на вход неопределенное
    количество аргументом и возвращающая сумму args[i] * i
    Пример: args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10
"""
def sum_elements(*args):
    sum = 0
    for i, j in enumerate(args[0]):
        sum += i * int(j)
    return sum

s_list = input('Input arguments (use space): ')
list_arguments = tuple(s_list.split())
print(sum_elements(list_arguments))














