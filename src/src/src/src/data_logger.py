class DataLogger:
    def __init__(self):
        self.zones = {}
        self.sensors = []

    def register_zone(self, zone):
        self.zones[zone.name] = zone

    def register_sensor(self, sensor):
        self.sensors.append(sensor)

    def log_measurement(self, measurement):
        zone = self.zones.get(measurement.zone_name)
        if zone:
            zone.add_measurement(measurement)
