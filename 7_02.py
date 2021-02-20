"""
    Задание 7.02
    Написать программу для работы с матрицами:
    1. Создание
    2. Вывод
    3. Сумма всех элементов
    4. Нахождение максимального элемента
    5. Нахождение минимального элемента.
"""
from random import randint
def matr(n, m):
    k = 0
    mat = []
    for i in range(m):
        a = []
        for j in range(n):
            k = randint(0, 9)
            a.append(k)
        mat.append(a)
    return mat

def print_matr(matr):
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            print(matr[i][j],end=' ')
        print()

def sum_elements(matr):
    sum = 0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            sum += matr[i][j]
    return sum

def max_matr(matr):
    max_ = 0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if matr[i][j] >= max_:
                max_ = matr[i][j]
    return max_

def min_matr(matr):
    min_ = matr[0][0]
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if matr[i][j] <= min_:
                min_ = matr[i][j]
    return min_

n = int(input('Input n: '))
m = int(input('Input m: '))
mat = matr(n, m)
print(f'matrix = {mat}')
mat_print = print_matr(mat)
summ = sum_elements(mat)
print(f'summ = {summ}')
maxx = max_matr(mat)
print(f'max = {maxx}')
minn = min_matr(mat)
print(f'min = {minn}')








