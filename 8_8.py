# Given an array of integers A.
# Find the sum of #the positive and negative elements of the array using the sum function.

def sum_foo(list):
    sum = 0
    for i in list:
        sum += i
    return sum
list_numbers = list(map(int, input('Input numbers here with space: ').split()))
list_positives = list(filter(lambda x: x > 0, list_numbers))
list_negatives = list(filter(lambda x: x < 0, list_numbers))
print(f'sum of positives numbers: {sum_foo(list_positives)}')
print(f'sum of negatives numbers: {sum_foo(list_negatives)}')