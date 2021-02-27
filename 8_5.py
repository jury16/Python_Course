#A list of numbers is given. Count how many times each number occurs.

list_numbers=list(map(str, input('Input numbers with space: ').split()))
dict_numbers = {}

for i in list_numbers:
    if i not in dict_numbers:
        dict_numbers[i] = 1
    else:
        dict_numbers [i] += 1
number = int(input('Input number to check: '))
print(dict_numbers.get(str(number), None))