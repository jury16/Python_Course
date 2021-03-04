"""
Write a generator that will take a file name as input
and generate it line by line (i.e. yield of each line).
"""


def read_file(file):
    my_file = open(file, 'r')
    while True:
        while True:
            line = my_file.readline()
            yield line
            if not line:
                break
            #print(line, end='')
        my_file.close()

val = read_file('text.txt')
print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))
