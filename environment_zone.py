class EnvironmentZone:
    def __init__(self, name):
        self.name = name
        self.measurements = []

    def add_measurement(self, measurement):
        self.measurements.append(measurement)

    def get_values(self):
        return [m.value for m in self.measurements]
