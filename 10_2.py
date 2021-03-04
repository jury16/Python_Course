"""
Create a text file and write 6 lines to it.
The lines to be written are entered from the keyboard.
"""


with open('text_write.txt', "w") as my_file:
    for i in range(5):
        my_file.write(input('Input string: ') +'\n')



