"""
    Задание 4.04
    Ввести с клавиатуры целое число n. Получить
    сумму кубов всех целых чисел от 1 до
    n(включая n) используя цикл while 
"""
num = int(input('Input number: '))
sums = 0
count = 0
while count <= num:
    sums += count
    count += 1
print(f'sum = {sums}')





