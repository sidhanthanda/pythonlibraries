import json
import pprint as pp


with open('true_json.json') as d:
    data = json.load(d)


pp.pprint(data)


print(data["students"][0]["id"])
print(data["students"][0]["name"])
print(data["students"][0]["age"])
print(data["students"][0]["full-time"])


print(data["students2"][0]["id"])
print(data["students2"][0]["name"])
print(data["students2"][0]["age"])
print(data["students2"][0]["full-time"])
