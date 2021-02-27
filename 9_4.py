#A list of numbers is given. Find the product of all
#numbers that are multiples of 3.

from functools import reduce
list_numbers = list(map(int, input('Input names here with space: ').split()))
result = reduce(lambda a, x: a * x , filter(lambda x: not x % 3, list_numbers))
print(result)

