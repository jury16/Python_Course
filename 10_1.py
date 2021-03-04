"""
There is a text file. Type:
a) its first line;
b) its fifth line;
c) its first 5 lines;
d) its lines from s1 through s2;
e) the whole file.
"""


my_file = open('text.txt')


print(f'first line:\n{my_file.readline()}')
print(f'fifth line:\n{my_file.readlines()[4]}')
print(f'first 5 lines:', end='')
my_file.close()

for i, line in enumerate(open('text.txt')):
    if  i <= 4:
        print(line, end='')

my_file.close()

my_file = open('text.txt')
s1 = int(input('input s1: '))
s2 = int(input('input s2: '))
print(f'lines from {s1} to {s2}:')

for i, line in enumerate(my_file):
    if  i in range(s1, s2):
        print(line, end='')
my_file.close()

my_file = open('text.txt')

print(f'all file:')
while True:
    line = my_file.readline()
    if not line:
        break
    print(line, end='')
my_file.close()


