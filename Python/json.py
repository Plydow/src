"""
json is standart python librairy to load and save information in json format
"""

#python version
all

#install
python -m pip install json

#docs
https://docs.python.org/3/library/json.html
https://tools.ietf.org/html/rfc8259

#use
"importation of modules"
import json

"load from file"
with open(file_path, 'r') as file:
    data = json.load(file)

"load from string"
data = json.loads(string)

"save to file"
with open(file_path, 'w') as file:
    json.dump(data, file)

"convert to string"
string = json.dumps(data)
