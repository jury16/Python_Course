"""
    Задание 5.01
    Создать квадратную матрицу размерностью n
    и заполнить ее случайными значениями от 1
    до 9.
"""
from random import randint
n = int(input('Input n: '))
matr = []
for i in range(n):
    a = []
    for j in range(n):
        a.append(randint(0, 9))
    matr.append(a)
print(f'matrix = {matr}')





