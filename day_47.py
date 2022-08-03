# Day 47: Save a JSON
# Write a function called save_json. This function takes a dictionary
# below as an argument and saves it on a file in JSON format.
# Write another function called read_json that opens the file that you
# just saved and reads its content.
import json

names = {'name': 'Carol','sex': 'female','age': 55}

def save_json():
    with open('data.json', 'w') as file:
        obj = json.dumps(names, indent = 4)
        json.dump(obj, file)
        return obj

def read_json():
    with open('data.json', 'r') as file:
        data = json.load(file)
        return data

print(save_json()) # prints initial json file
print(read_json()) # prints json file after opening
