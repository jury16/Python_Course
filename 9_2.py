#Create a lambda function that takes a list of names as
# input and outputs them in the format “Hello, {name}” to another list

list_names = list(map(str, input('Input names here with space: ').split()))
answer = list(map(lambda x: f'Hello, {x}!', list_names))
print(answer)

