
"""
    Задания 3.11
    Ввести почтовый адрес. Проверить доменной имя. В случае если оно
    gmail.com, вывести на экран имя почтового ящика. Иначе вывести надпись
    “DOMAIN NAME is not supported’
"""
s = input('Input e-mail:    ')
if '@' in s:
    num = s.index('@')
    if s[num + 1:] == 'gmail.com':
        print(s)
    else:
        print('DOMAIN NAME is not supported')
else:
    print('E-mail not valid!')







