"""
    Пример 7.01
    Написать функцию, которая получает на вход
    имя и выводит строку вида: “Hello, {name}”.
    Создать список из 5 имен. Вызвать функцию
    для каждого элемента списка в цикле.
"""
def hello(name):
    return print(f'Hello, {name}!')

names = ['Yuri', 'Ivan', 'Nata', 'Gala', 'Ira']
for i in names:
    hello(i)

