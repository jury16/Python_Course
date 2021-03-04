"""
There is a text file. Overwrite all its lines to another file,
replacing the character 0 with the character 1 and vice versa.
"""
with open('text_zeros_ones_wright.txt', "w") as my_file_wright:
    with open('text_zeros_ones_read.txt', "r") as my_file_read:
        while True:
            line = my_file_read.readline()
            if not line:
                break
            my_file_wright.write(line.replace('0','1'))

with open('text_zeros_ones_wright.txt', "r") as my_file_wright:
    with open('text_zeros_ones_read.txt', "w") as my_file_read:
        while True:
            line = my_file_wright.readline()
            if not line:
                break
            my_file_read.write(line.replace('1','0'))





