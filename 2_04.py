"""
    Задание 2.04
    Создать два списка a = [1,2,3,4] и b = [ ]
    Вывести на экран id a и b
    Присвоить b значение a (b=a)
    Вывести на экран id переменных
    Добавить элемент в список b
    Вывести на экран оба списка
"""
a = [1, 2, 3, 4]
b = []
b = a
print(f'id(a) = {id(a)}')
print(f'id(b) = {id(b)}')
b.append(8)
print(f'a = {a}')
print(f'b = {b}')