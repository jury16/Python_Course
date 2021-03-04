"""
There is a text file. Write all even lines of this file to the second file,
and all odd lines to the third file. The order of the lines is preserved.
"""
with open('text_2.txt', "w") as my_file_2:
    with open('text_3.txt', "w") as my_file_3:
        with open('text_1.txt', "r") as my_file_1:
            count = 0
            while True:
                line = my_file_1.readline()
                if not line:
                    break
                elif count % 2:
                    my_file_3.write(line)
                else:
                    my_file_2.write(line)
                count += 1







