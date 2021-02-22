"""
Enter a string. If the line length is more
than 10 characters, then create a new line
with 3 exclamation marks at the end ('!!!')
and display it. If less than 10, then display
the second character of the string
"""
s = input('Input string: ')
if len(s) > 10:
    s1 = s + '!!!'
    print(s1)
else:
    print(s[1])
