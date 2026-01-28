class AlertSystem:
    def __init__(self):
        self.thresholds = {
            "temperature": 40,
            "air": 150,
            "water": 8.5
        }

    def check_alert(self, sensor_type, value):
        limit = self.thresholds.get(sensor_type)

        if limit and value > limit:
            return f"⚠ ALERT: {sensor_type.upper()} value {value:.2f} exceeded safe limit {limit}"
        return None
