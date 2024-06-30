import json
import os
import pathlib
import pprint as pp 


def get_json_document(json_file_name):
    json_file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), json_file_name)
    with open (json_file_path, "r") as json_file:
        json_doc = json.load(json_file)              
        return  json_doc

def get_weights_from_json_document(json_doc):    
    students = json_doc["students"]
    # student_1 = students[0]
    # weight_of_student_1 = student_1["weight"]
    # return weight_of_student_1

    total_weight=0

    for student in students:
       student_weight = int(student["weight"])
       total_weight = total_weight +student_weight

    return total_weight
    

#-------------------------------------------------------------
#1
json_document = get_json_document("june_data.json")

#2
total_weights = get_weights_from_json_document(json_document)

pp.pp("Total weight of all students is : " + str(total_weights)) 




