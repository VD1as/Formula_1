class Constructor:
    def __init__(self, constructor_id, name, nationality):
        self.constructor_id = constructor_id
        self.name = name
        self.nationality = nationality

    def __str__(self):
        return self.name
