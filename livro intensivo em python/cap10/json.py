import json

numbers = [2, 5, 7, 9, 2, 3, 6, 13]
filename = 'cap10/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
