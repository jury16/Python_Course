"""
    Задание 4.02
    Просуммировать неопределенное количество чисел,
    вводимых пользователем, суммировать до тех пор, пока
    пользователь не введёт слово «стоп»
"""
s = input('Input numbers: ')
sums = 0
while s != 'stop':
    sums += int(s)
    s = input('Input numbers: ')
print(f'sum = {sums}')





