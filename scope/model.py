import yaml

with open("scope/db/db.yml", "r") as f:
    data = yaml.full_load(f)


class ScopeZM:
    all_provinces = [p["name"] for p in data]

    def __init__(self, provinces=all_provinces) -> None:
        self.provinces = provinces
        self.size = len(provinces)

    def get_all_provinces(self) -> list:
        return self.provinces

    def current_province(self):
        pass

    def cities(self, province: str) -> list:
        for p in data:
            if province.lower() == p["name"] or province.lower() in p["name"]:
                return sorted(p["towns"])
        return []

    def number_of_provinces(self) -> int:
        return self.size

    # Get towns in each province
    def towns_in_central(self) -> list:
        return sorted(data[0]["towns"])

    def towns_in_copperbelt(self) -> list:
        return sorted(data[1]["towns"])

    def towns_in_eastern(self) -> list:
        return sorted(data[2]["towns"])

    def towns_in_luapula(self) -> list:
        return sorted(data[3]["towns"])

    def towns_in_lusaka(self) -> list:
        return sorted(data[4]["towns"])

    def towns_in_muchinga(self) -> list:
        return sorted(data[5]["towns"])

    def towns_in_northern(self) -> list:
        return sorted(data[6]["towns"])

    def towns_in_north_western(self) -> list:
        return sorted(data[7]["towns"])

    def towns_in_southern(self) -> list:
        return sorted(data[8]["towns"])

    def towns_in_western(self) -> list:
        return sorted(data[9]["towns"])

    # to search for province by city
    def find_province_by_city(self, city: str) -> str:
        for p in data:
            if city.capitalize() in p["towns"]:
                return f"{p["name"]}".capitalize()
        return f"{city} was not found. Check you spelling"

    def get(self, province=None, city=None):
        if province is None and city is None:
            return []
        if province is None:
            return self.find_province_by_city(city=str(city))
        if city is None:
            return self.get_all_provinces()
