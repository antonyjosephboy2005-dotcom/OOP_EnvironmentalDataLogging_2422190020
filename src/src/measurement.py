from datetime import datetime

class Measurement:
    def __init__(self, sensor_id, value, zone_name):
        self.sensor_id = sensor_id
        self.value = value
        self.zone_name = zone_name
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.zone_name}: {self.value:.2f} at {self.timestamp}"
