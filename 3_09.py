
"""
    Задания 3.09
    Вычислить квадратное уравнение ax2
    + bx + c = 0 (*)
    D = b2
    – 4ac;
    x1,2 = (-b +/- sqrt (D)) / 2a
    Предусмотреть 3 варианта:
    1) Два действительных корня
    2) Один действительный корень
    3) Нет действительных корней
"""
a = int(input('Input a =   '))
b = int(input('Input b =   '))
c = int(input('Input c =   '))
D = b**2 - 4 * a * c
if D > 0 and a != 0:
    print(f'x1 = {(-b + D)/(2 * a)}, x2 = {(-b - D)/(2 * a)}')
elif D == 0 and a != 0:
    print(f'x1,2 = {-b/(2 * a)}')
else:
    print('No valid roots')


