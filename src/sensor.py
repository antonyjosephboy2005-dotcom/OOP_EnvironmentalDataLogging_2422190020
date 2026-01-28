import random

class Sensor:
    def __init__(self, sensor_id, sensor_type, unit, zone_name):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.unit = unit
        self.zone_name = zone_name

    def generate_reading(self):
        """Simulate sensor data based on sensor type"""
        if self.sensor_type == "temperature":
            return random.uniform(20, 45)

        elif self.sensor_type == "air":
            return random.uniform(50, 200)

        elif self.sensor_type == "water":
            return random.uniform(6, 9)

        return 0
