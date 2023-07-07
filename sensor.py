import random
from datetime import datetime

class Sensor:
    def __init__(self, min_value, max_value,name):
        self.min_value = min_value
        self.max_value = max_value
        self.name = name
    def read_data(self):
        return (datetime.now(), random.uniform(self.min_value, self.max_value))

# i couldnt think of specific implementation for the subclasses
class TemperatureSensor(Sensor):
    pass

class HumiditySensor(Sensor):
    pass

class LightSensor(Sensor):
    pass