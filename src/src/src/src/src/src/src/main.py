from sensor import Sensor
from measurement import Measurement
from environment_zone import EnvironmentZone
from data_logger import DataLogger
from algorithms import zone_statistics

# Create zones
zone_a = EnvironmentZone("Zone A")
zone_b = EnvironmentZone("Zone B")

# Create logger
logger = DataLogger()
logger.register_zone(zone_a)
logger.register_zone(zone_b)

# Create sensors
sensor1 = Sensor("S1", "temperature", "°C", "Zone A")
sensor2 = Sensor("S2", "air", "AQI", "Zone B")

logger.register_sensor(sensor1)
logger.register_sensor(sensor2)

print("\n--- Stage 2 Simulation Running ---\n")

# Generate and log measurements
for sensor in logger.sensors:
    value = sensor.generate_reading()
    m = Measurement(sensor.sensor_id, value, sensor.zone_name)

    logger.log_measurement(m)
    print(m)

# Display zone statistics
print("\n--- Zone Statistics ---")
for zone in logger.zones.values():
    stats = zone_statistics(zone)
    print(zone.name, stats)
