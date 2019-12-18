import json

with open('predefini.txt') as json_file:
    data = json.load(json_file)

print(data)
