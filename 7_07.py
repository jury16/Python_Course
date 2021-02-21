"""
Задание 7.07
Создать функцию, которая принимает на вход
неопределенное количество именных
аргументов и выводит на экран те из них,
длина ключа которых четна.
"""
def my_func(**kwargs):
    for key, value in kwargs.items():
        if not len(key) % 2:
            print("%s : %s" %(key, value))

my_func(aasa='ttt', fgf=3, lo="sdaasda")















