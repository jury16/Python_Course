
"""
    Задания 3.10
    Получить на ввод количество рублей и копеек и вывести в правильной
    форме, например, 3 рубля, 1 рубль 25 копеек, 3 копейки
"""
s = input('Input rubs and cops:    ')
rub = s.split()[0]
kop = s.split()[1]
rubs = ''
kops = ''
if 9 < int(rub) % 100 < 20 or 4 < int(rub) % 10 < 10 or int(rub) % 10 == 0:
    rubs = 'рублей'

elif 1 < int(rub) % 10 < 5 :
    rubs = 'рубля'

else:
    rubs = 'рубль'

if 9 < int(kop) % 100 < 20 or 4 < int(kop) % 10 < 10 or int(kop) % 10 == 0:
    kops = 'копеек'

elif 1 < int(kop) % 10 < 5 :
    kops = 'копейки'

else:
    kops = 'копейка'

print(f'{rub} {rubs} {kop} {kops}' )





