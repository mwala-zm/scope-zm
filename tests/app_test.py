import yaml

with open("scope/db/db.yml", "r") as f:
    data = yaml.full_load(f)


# for province in data:
#    print(province["name"])

def get_towns(province: str):
    for item in data:
        if item["name"] == province.lower() or province.lower() in item["name"]:
            return item["towns"]
