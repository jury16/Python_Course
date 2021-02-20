"""
    Задание 4.07
    Ввести два целых числа A и B ( A < B ). Вывести в порядке
    возрастания все целые числа, расположенные между A и
    B (включая сами числа A и B ), а также количество N этих 
    чисел. [01-08-For2]
"""
a = int(input('Input a: '))
b = int(input('Input b: '))
count = 0
for i in range(a, b + 1):
    count += 1
    print(i)
print(f'count = {count}')





