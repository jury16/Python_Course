"""
    Задание 4.06
    Получить сумму кубов натуральных чисел от n
    до m используя цикл for
"""
n = int(input('Input n: '))
m = int(input('Input m: '))
if n > m:
    n, m = m, n
sum = 0
for i in range(n, m):
    sum += i**3
print(sum)





