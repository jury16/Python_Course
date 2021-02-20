"""
    Дан двумерный массив n × m элементов. Определить,
    сколько раз встречается число 7 среди элементов
    массива.[02-4.2-BL12]
"""
from random import randint
n = int(input('Input n: '))
m = int(input('Input m: '))
matr = []
i = 0
k = 0
sum_7 = 0
for i in range(m):
    a = []
    for j in range(n):
        k = randint(0, 9)
        a.append(k)
        if k == 7:
            sum_7 += 1
    matr.append(a)
print(f'matrix = {matr}')
print(f'sum_7 = {sum_7}')





