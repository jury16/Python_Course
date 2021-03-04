"""
Add three new lines of text to the end of the existing text file.
The lines to be written are entered from the keyboard.
"""


with open('text_write.txt', "a") as my_file:
    for i in range(3):
        my_file.write(input('Input string: ') +'\n')



