"""
    Задание 2.03
    Создать список из двух элементов.
    Создать кортеж из двух элементов.
    Создать словарь с одной парой. Ключ - кортеж, значение - список
    Создать словарь с одной парой. Ключ - список, значение - кортеж
"""
list_of_two = [1, 2]
tuple_of_two = ('a', 'b')
#dict_1 = {list_of_two:tuple_of_two}   #gives error
dict_2 = {tuple_of_two:list_of_two}
print('list: ', list_of_two)
print('tuple: ', tuple_of_two)
#print('dict_1: ', dict_1)
print('dict_2: ',dict_2)
