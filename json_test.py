import json
import random

numbers = [i for i in range(27) if i%3 == 0]
filename = input("Enter file to save: ")

try:
    with open(filename, 'w') as f:
        json.dump(numbers, f)
except FileNotFoundError:
    print(f'File not found! ')
else:
    print(f'Date succesfully saved at {filename}  file')

try:
    with open(filename) as  file:
        data = json.load(file)
except FileNotFoundError:
        print(f'File not found')
else:
    print(f'Read file : {data}')
