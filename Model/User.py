class User:
    __slots__ = ["id", "username", "password", "carbon_footprint"]

    def __init__(self, id, username, password, carbon_footprint):
        self.id = id
        self.username = username
        self.password = password
        self.carbon_footprint = carbon_footprint