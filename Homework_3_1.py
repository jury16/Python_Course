"""
Enter the number.
If this number is divisible by 1000 without a remainder,
then display the "millennium"
"""
s = int(input())
if not s % 1000:
    print("millennium")
