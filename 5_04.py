"""
    Задание 5.04
    Дана целочисленная матрица А[n,m]. Посчитать
    количество элементов матрицы, превосходящих среднее
    арифметическое значение элементов матрицы и сумма
    индексов которых четна.[02-4.2-BL23]
"""
from random import randint
n = int(input('Input n: '))
m = int(input('Input m: '))
matr = []
i = 0
sum_average = 0
k = 0
sum_elements = 0
for i in range(m):
    a = []
    for j in range(n):
        k = randint(0, 100)
        a.append(k)
        sum_average  += k
    matr.append(a)
sum_average = sum_average / (n * m)
for i in range(m):
    for j in range(n):

        if matr[i][j] > sum_average and not (i + j) % 2:
            sum_elements += 1
print(f'matrix = {matr}')
print(f'sum_average = {sum_average}')
print(f'sum_elements = {sum_elements}')






