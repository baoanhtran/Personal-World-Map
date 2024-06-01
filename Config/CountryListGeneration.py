import json

def country_to_list():
    with open("Database/ExternalData/country_shapes.json", "r") as f:
        data = json.load(f)
        countries = []
        for i, ele in enumerate(data):
            dico = {
                "id": i+1,
                "name": ele["cntry_name"],
                "description": ""
            }
            countries.append(dico)

    countries.sort(key=lambda x: x["name"])  # Sort countries by name

def sort_countries():
    with open("Database/Entity/countries.json", "r") as f:
        data = json.load(f)
        data.sort(key=lambda x: x["name"])  # Sort countries by name

        # Update the id of each country
        for i, ele in enumerate(data):
            ele["id"] = i+1

    with open("Database/Entity/countries.json", "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    sort_countries()