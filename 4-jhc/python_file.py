import json
import pprint as pp
import os
import pathlib


# reusable functions ------------------------------------------------------------------------------------------
def open_file_by_name(file_name):    

    file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), file_name)

    with open (file_path, "r") as json_file:
        json_doc = json.load(json_file)
        return json_doc
  
def get_student_name_by_index(index, json_doc):
    students= json_doc["students"]
    student_1 = students[index]
    name_of_student_1 = student_1["name"]
    return name_of_student_1

def get_file_name():
    file_name= input("Enter name of file : ")
    return file_name
   
def take_weight_from_thing(index, json_doc):
    students = json_doc["students"]    
    student_1 = students[index]
    weight_of_student_1 = student_1["weight"]
    return weight_of_student_1

def take_weiight_from_thing(index, json_doc):
    students = json_doc["students"]
    student_2 = students[index]
    weight_of_student_2 = student_2["weight"]
    return weight_of_student_2

# execution sequence  -----------------------------------------------------------------------------------------

file_name = get_file_name()

doc= open_file_by_name(file_name)

name = get_student_name_by_index(0, doc)
    
weight = take_weight_from_thing(0, doc)
w3ight = take_weiight_from_thing(1, doc)

pp.pp(name)
pp.pp(weight)
pp.pp(w3ight)
