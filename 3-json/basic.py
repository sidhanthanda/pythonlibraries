import json
import os
import pprint



data_in_file=""
file_name= "plain_text.txt"


with open(file_name) as just_a_regular_file:
    data_in_file = just_a_regular_file.read()
    
print("read contents of json file as a regular file")
print(data_in_file)
print("-------------------------------------------------")
print("")


#create json object
print("load the contents of the file into a json document")
json_document = json.loads(data_in_file)
print(json_document)
print("-------------------------------------------------")





