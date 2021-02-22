"""
Enter the string. Display the letter in the
middle of this string. Also, if this center letter
is equal to the first letter in the string, then
create and print the part of the string between
the first and last characters of the original string.
(hint: to get the center letter, find the length
of the string and split it in half. To create the
resulting string, use a slice)
"""
s = input('Input string: ')
position = len(s) // 2
if s[position + 1] == s[1]:
    print(s[1: -1])
elif not len(s) % 2:
    print(f'in the middle of the line two letters: {s[position - 1]} and {s[position]}')
else:
    print(s[position])
