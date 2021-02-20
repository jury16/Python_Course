"""
    Задание 5.07
    Написать игру. Пользователь должен угадать число.
    Сперва вводиться диапазон угадывания. После
    колличество попыток. В случае правильного ответа -
    выводить You are the winner. В случае неправильного
    давать игроку подсказку(больше или меньше искомое
    число). Если за указанное количество попыток число не
    угадано - выводить: You are the loser и правильное число.
"""
from random import randint
number_range = input('Input range input with space:')
a = number_range.split()
answer  = randint(int(a[0]), int(a[1]))
attempt = 0
while attempt < 2:
    number = int(input('Input number '))
    print('number:', number)
    if not (number - answer):
        print(f'You are the winner! The number is {number}')
        break
    elif number < answer:
        print('more')
        attempt += 1
    elif number > answer:
        print('less')
        attempt += 1
    number = 0
else:
     print(f'You are the loser! The number is {number}')


