import json

def load_raw_coordinates():
    with open("Database/ExternalData/country_shapes.json", "r") as f:
        data = json.load(f)
        coordinates = {}
        for ele in data:
            coordinates[ele["cntry_name"]] = ele["geo_shape"]["geometry"]["coordinates"]

    with open("Database/ExternalData/raw_country_shapes.json", "w") as f:
        json.dump(coordinates, f, indent=4)

if __name__ == "__main__":
    load_raw_coordinates()