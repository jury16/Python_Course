"""
There is a wedding in the N family. They decided to choose the place
to celebrate depending on the number of people arriving in the morning.
If there are more than 50, they will order a restaurant, if there are
20 to 50 cafes, and if there are less than 20, then I will celebrate at home.
Display "restaurant", "cafe", "house" depending on the number of guests
(read the variable from the console)
"""
guests = int(input())
if guests > 50:
    print("restaurant")
elif 20 < guests <= 50:
    print("cafe")
else:
    print('house')