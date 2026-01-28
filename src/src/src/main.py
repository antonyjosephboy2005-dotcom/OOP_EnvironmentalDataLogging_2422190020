from sensor import Sensor
from measurement import Measurement
from environment_zone import EnvironmentZone
from data_logger import DataLogger
from algorithms import zone_statistics
from alert_system import AlertSystem
from trend_prediction import moving_average, predict_next

# Zones
zone_a = EnvironmentZone("Zone A")
zone_b = EnvironmentZone("Zone B")

# Logger
logger = DataLogger()
logger.register_zone(zone_a)
logger.register_zone(zone_b)

# Sensors
sensor1 = Sensor("S1", "temperature", "°C", "Zone A")
sensor2 = Sensor("S2", "air", "AQI", "Zone B")

logger.register_sensor(sensor1)
logger.register_sensor(sensor2)

# Alert System
alerts = AlertSystem()

print("\n--- Stage 3 Simulation Running ---\n")

# Collect multiple readings
for i in range(5):
    for sensor in logger.sensors:
        value = sensor.generate_reading()
        m = Measurement(sensor.sensor_id, value, sensor.zone_name)

        logger.log_measurement(m)
        print(m)

        # Alert Check
        alert = alerts.check_alert(sensor.sensor_type, value)
        if alert:
            print(alert)

# Trend + Prediction
print("\n--- Trend & Prediction ---")
for zone in logger.zones.values():
    values = zone.get_values()

    avg = moving_average(values)
    prediction = predict_next(values)

    print(f"{zone.name} Moving Avg: {avg}")
    print(f"{zone.name} Prediction: {prediction}")
