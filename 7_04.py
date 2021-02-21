"""
    Задание 7.04
    Реализовать функцию возвращающую
    матрицу. На вход принимает n - размерность
    матрицы, random_from(по-умолчанию 1),
    random_to(по-умолчанию(9)).
"""
from random import randint
def matrix_make(dimension, random_from = 1, random_to = 9):
    mat = []
    for i in range(dimension):
        a = []
        for j in range(dimension):
            a.append(randint(random_from, random_to))
        mat.append(a)
    return mat

n = int(input('Input n - dimension : '))
number_range = input('Input range input with space: ')
random = number_range.split()

if len(number_range) == 1:
    random1 = int(random[0])
    matrix_ = matrix_make(n, random1)
    print(f'matrix = {matrix_}')
elif not len(number_range):
    matrix_ = matrix_make(n)
    print(f'matrix = {matrix_}')
else:
    random = number_range.split()
    random1 = int(random [0])
    random2 = int(random [1])
    matrix_ = matrix_make(n, random1, random2)
    print(f'matrix = {matrix_}')















