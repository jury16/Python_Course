#convert inch to cm
def inch_cm(a):
    return f'{2.54 * a} cm'
#convert cm to inch
def cm_inch(a):
    return f' {(0.39 * a):.2f} inch'
#convert miles to km
def miles_km(a):
    return f' {(1.60934 * a):.2f}'
#convert km to miles
def km_miles(a):
    return f' {(0.621371 * a):.2f}'
#convert pound to kg
def pound_kg(a):
    return f' {(0.453592 * a):.2f}'
#convert kg to pound
def kg_pound(a):
    return f' {(2.20462 * a):.2f}'
#convert ounce to grams
def ounce_gram(a):
    return f' {(28.3495 * a):.2f}'
#convert gram to ounce
def gram_ounce(a):
    return f' {(0.035274 * a):.2f}'
#convert gallon to litre
def gallon_litre(a):
    return f' {(3.78541 * a):.2f}'
#convert litre to gallon
def litre_gallon(a):
    return f' {(0.2641720524 * a):.2f}'
#convert pint to litre
def pint_litre(a):
    return f' {(3.78541 * a):.2f}'
#convert litre to pint
def litre_pint(a):
    return f' {(0.2641720524 * a):.2f}'
print('#####Converot#####')
print('1 - Convert inch to cm')
print('2 - Convert cm to inch')
print('3 - Convert miles to km')
print('4 - Convert km to miles')
print('5 - Convert pound to kg')
print('6 - Convert kg to pound')
print('7 - Convert ounce to grams')
print('8 - Convert grams to ounce')
print('9 - Convert gallon to litre')
print('10 - Convert litre to gallon')
print('11 - Convert pint to litre')
print('12 - Convert litre to pint')
print(' 0 - Exit')
number_convertor = int(input('Input number of converter: '))

while number_convertor:
    number = int(input('Input number: '))
    if number_convertor == 1:
        print(f'{number} inch is {inch_cm(number)} cm\n')
    elif number_convertor == 2:
        print(f'{number} cm is {cm_inch(number)} inch\n')
    elif number_convertor == 3:
        print(f'{number} mile is {miles_km(number)}\n')
    elif number_convertor == 4:
        print(f'{number} km is {km_miles(number)} mile\n')
    elif number_convertor == 5:
        print(f'{number} pound is {pound_kg(number)} kg\n')
    elif number_convertor == 6:
        print(f'{number} kg is {kg_pound(number)} pound\n')
    elif number_convertor == 7:
        print(f'{number} ounce is {ounce_gram(number)} gram\n')
    elif number_convertor == 8:
        print(f'{number} gram is {gram_ounce(number)} ounce\n')
    elif number_convertor == 9:
        print(f'{number} gallon is {gallon_litre(number)} litre\n')
    elif number_convertor == 10:
        print(f'{number} litre is {litre_gallon(number)} gallon\n')
    elif number_convertor == 11:
        print(f'{number} pint is {pint_litre(number)} litre\n')
    elif number_convertor == 12:
        print(f'{number} litre is {litre_pint(number)} pint\n')
    else:
        print('Number convertor is not valid')
    number_convertor = int(input('Input number of converter: '))














