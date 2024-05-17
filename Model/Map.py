import json

class Map:
    __slots__ = ["l_canvas", "h_canvas", "coordinates_dict"]

    def __init__(self, l_canvas, h_canvas):
        self.l_canvas = l_canvas
        self.h_canvas = h_canvas
        self.load_coordinates(l_canvas, h_canvas)

    def load_coordinates(self, l_canvas, h_canvas):
        with open("Database/ExternalData/raw_country_shapes.json", "r") as f:
            data = json.load(f)
            coordinates = {}
            for key, value in data.items():
                coordinates[key] = self.convert_whole_coordinates(value, l_canvas, h_canvas)

        self.coordinates_dict = coordinates

    def xy_from_lat_long(self, latitude, longitude, l_canvas, h_canvas):
        x = (longitude + 180) * (l_canvas / 360)
        y = h_canvas - (latitude + 90) * (h_canvas / 180)
        return x, y

    def convert_whole_coordinates(self, coordinates, l_canvas, h_canvas):
        if self.list_depth(coordinates) == 4: # Corresponds to multipolygon coordinates
            for ele in coordinates:
                for ele2 in ele:
                    for ele3 in ele2:
                        lng, lat = ele3
                        x, y = self.xy_from_lat_long(lat, lng, l_canvas, h_canvas)
                        ele3[0] = x
                        ele3[1] = y
        elif self.list_depth(coordinates) == 3: # Corresponds to polygon coordinates
            for ele in coordinates:
                for ele2 in ele:
                    lng, lat = ele2
                    x, y = self.xy_from_lat_long(lat, lng, l_canvas, h_canvas)
                    ele2[0] = x
                    ele2[1] = y

        return coordinates

    def list_depth(self, lst):
        if not isinstance(lst, list):
            return 0
        return 1 + max(self.list_depth(item) for item in lst)