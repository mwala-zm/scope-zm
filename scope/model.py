import yaml

with open("scope/db/db.yml", "r") as f:
    data = yaml.full_load(f)

class ScopeZM:
    get_provinces = ""

    def __init__(self, provinces, cities) -> None:
        self.provinces = provinces
        self.cities = cities

    def provinces(self):
        for p in data:
            return p["name"]

    def current_province(self):
        pass

    def cities(self, province):
        for cities in province:
            return cities

    def get(self, province=None, city=None):
        if province == None:
            return self.provinces
        elif city == None:
            return self.cities
