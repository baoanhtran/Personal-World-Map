import json

class Map:
    """
    Represents a map with coordinates for visualization.
    """

    __slots__ = ["l_canvas", "h_canvas", "coordinates_dict"]

    def __init__(self, l_canvas, h_canvas):
        """
        Initializes the Map object.

        Args:
            l_canvas (int): Width of the canvas.
            h_canvas (int): Height of the canvas.
        """
        self.l_canvas = l_canvas
        self.h_canvas = h_canvas
        self.load_coordinates(l_canvas, h_canvas)

    def load_coordinates(self, l_canvas, h_canvas):
        """
        Loads coordinates from a JSON file and converts them to canvas coordinates.

        Args:
            l_canvas (int): Width of the canvas.
            h_canvas (int): Height of the canvas.
        """
        with open("Database/ExternalData/raw_country_shapes.json", "r") as f:
            data = json.load(f)
            coordinates = {}
            for key, value in data.items():
                coordinates[key] = self.convert_whole_coordinates(value, l_canvas, h_canvas)

        self.coordinates_dict = coordinates

    def xy_from_lat_long(self, latitude, longitude, l_canvas, h_canvas):
        """
        Converts latitude and longitude to canvas coordinates.

        Args:
            latitude (float): Latitude.
            longitude (float): Longitude.
            l_canvas (int): Width of the canvas.
            h_canvas (int): Height of the canvas.

        Returns:
            tuple: Canvas coordinates (x, y).
        """
        x = (longitude + 180) * (l_canvas / 360)
        y = h_canvas - (latitude + 90) * (h_canvas / 180)
        return x, y

    def convert_whole_coordinates(self, coordinates, l_canvas, h_canvas):
        """
        Converts all coordinates in a data structure to canvas coordinates.

        Args:
            coordinates (list or dict): Coordinates data structure.
            l_canvas (int): Width of the canvas.
            h_canvas (int): Height of the canvas.

        Returns:
            list or dict: Converted coordinates.
        """
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
        """
        Determines the depth of a nested list.

        Args:
            lst (list): The nested list.

        Returns:
            int: The depth of the list.
        """
        if not isinstance(lst, list):
            return 0
        return 1 + max(self.list_depth(item) for item in lst)