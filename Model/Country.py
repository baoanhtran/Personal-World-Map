class Country:
    __slots__ = ["id", "name", "description"]

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
    
    def __eq__(self, other):
        return self.id == other.id