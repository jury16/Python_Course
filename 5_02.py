"""
    Задание 5.02
    Создать квадратную матрицу размерностью n
    и заполнить ее случайными значениями.
    Найти сумму всех элементов матрицы,
    которые кратны 3.
"""

from random import randint
n = int(input('Input n: '))
matr = []
k = 0
sum = 0
for i in range(n):
    a = []
    for j in range(n):
        k = randint(0, 9)
        a.append(k)
        if not k % 3:
            sum += k

    matr.append(a)

print(f'matrix = {matr}')
print(f'sum = {sum}')





