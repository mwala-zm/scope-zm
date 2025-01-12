import json

with open('db.json', 'r') as file:
    data = json.load(file)

provinces = data["provinces"]

def get__provinces_length():
    return len(provinces)

def get__provinces():
    for province in provinces:
        province["name"]

print(get__provinces_length())
