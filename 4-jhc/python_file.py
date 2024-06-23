import json

file = "redo.json"

with open (file, "r") as json_file:
    data = json.load(json_file)
    print(data)
    