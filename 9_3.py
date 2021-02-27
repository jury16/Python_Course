#Given a list of names, filter out all names,
#where is the letter k

list_names = list(map(str, input('Input names here with space: ').split()))
answer = list(filter(lambda x: 'k' in x , list_names))
print(answer)

