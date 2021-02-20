"""
    Задание 2.05
    1. Создать строку равную третьему символу введенной строки.
    2. Создать строку равную последнему символу введенной строки.
    3. Создать строку равную первым пяти символам введенной строки.
    4. Создать строку равную введенной строки без последних двух символов.
    5. Создать строку равную всем элементам введенной строки с четными индексами.
"""
s = input('input string : ')
third_string = s[2]
last_string = s[-1]
first_five = s[:5]
without_two = s[:-2]
even_string = s[::2]
print(f'third_string = {third_string}')
print(f'last_string = {last_string}')
print(f'first_five = {first_five}')
print(f'without_two = {without_two}')
print(f'even_string = {even_string}')


