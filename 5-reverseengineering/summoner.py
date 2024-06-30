import json
import pprint as pp

# Functions

def obtain_file_name():
    filename = input("Enter your file name: ")
    return filename

def summon_json_file(filename):
    with open(filename, "r") as file:
        json_thing = json.load(file)
        return json_thing

def call_name(index, json_thing):
    names = (json_thing["name"])
    name = (json_thing["0"])
    return name

# Code
filename = obtain_file_name()

selected_doc = summon_json_file(filename)
pp.pprint(selected_doc)

name_of_thing = call_name(0, selected_doc)