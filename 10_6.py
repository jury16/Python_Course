"""
There are two text files with the same number of lines. Find out if their strings are the same.
If not, then get the number of the first line in which these files differ from each other.
"""

with open('text_10_6_2.txt', "r") as my_file_2:
    with open('text_10_6_1.txt', "r") as my_file_1:
        count = 0
        while True:
            line = my_file_1.readline()
            line1 = my_file_2.readline()
            if not line:
                print('The lines are the sames')
                break
            if line != line1:
                print(count)
            else:
                count  += 1









