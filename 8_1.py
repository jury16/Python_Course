#A list of words is given.
# Generate a new list with inverted words

list_=list(map(str, input('Input words with space: ').split()))

print(list(map(lambda x: x[::-1], list_)))
