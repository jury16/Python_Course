#A list of dictionaries is given. Each dictionary describes the
# machine (serial number and year of manufacture). Create a new
# list with all cars with a production year greater than n



list_dict = [{'age': 1999, 'number': 365},
            {'age': 2015, 'number': 4568},
            {'age': 2020, 'number': 98456}
             ]
new_list = [car for car in list_dict if car['age'] > 2000]
print(*new_list)