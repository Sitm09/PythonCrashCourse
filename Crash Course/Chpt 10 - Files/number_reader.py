import json

filename = 'Chpt 10 - Files/numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
