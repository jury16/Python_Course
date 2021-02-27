#A list of dictionaries is given. Each dictionary describes the
# machine (serial number and year of manufacture). Create a new
# list with all cars with a production year greater than n



old_dict = {'aa': 1, 'b': 2, 'cc': 3}
new_dict = {str(value): key for
key, value in old_dict.items()}
print(new_dict)