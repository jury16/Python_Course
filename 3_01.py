"""
    Задание 3.01
    Ввести с клавиатуры имя пользователя.
    Вывести на экран “Hello, [name]!”
"""
name = input('input Name : ')
print(f'Hello, {name}')
"""
    Задание 3.02
    Запросить у пользователя два целых числа.
    Вывести строку вида “2 плюс 3 равно 5”
"""
a = int(input('input first number : '))
b = int(input('input second number : '))
print(f'{a} + {b} = {a+b}')

"""
    Задание 3.03
    Ввести предложение состоящее из двух слов. Поменять
    местами слова, добавить восклицательный знак в начало
    и конец, вывести итоговое предложение на экран.
"""
s = input('input string:  ')
s = s.split()
print(f'!{s[1]} {s[0]}!')
