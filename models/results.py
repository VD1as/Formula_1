from models.drivers import drivers_data
from models.circuits import circuits_data
from models.constructor import constructor_data


class results(drivers_data, circuits_data, constructor_data):
    def __init__(self, race, circuit, driver, constructor):
        super(circuits_data).__init__(circuit)
        super(drivers_data).__init__(driver)
        super(constructor_data).__init__(constructor)