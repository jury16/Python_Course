"""
    Задание 3.04
    Ввести предложение. Если число символов в
    предложении кратно 3 - добавить ! к концу строки.
    Вывести строку на экран.
"""
s = input('input string: ')
if not len(s) % 3:
    print(f's!')
"""
    Задание 3.05
    Ввести предложение. Если в предложении есть слово
    code - вывести на экран Yes, иначе вывести на экран No
"""
s = input('input string:   ')
print('Yes' if 'code' in s else 'No')
"""
    Задание 3.06
    Запросить у пользователя возраст. Если возраст меньше
    0 - вывести Wrong input, если меньше 18 - вывести
    CocaCola, иначе - вывести Beer
"""
age = int(input('What is your age?   '))
print('CocaCola' if age < 18 else 'Beer')