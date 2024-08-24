class Driver:
    def __init__(self, driver_id, driver_ref, name, nationality, dob, number=None, code=None):
        self.driver_id = driver_id
        self.driver_ref = driver_ref
        self.name = name
        self.nationality = nationality
        self.dob = dob
        self.number = number
        self.code = code

    def __str__(self):
        return f"{self.name} ({self.nationality})"