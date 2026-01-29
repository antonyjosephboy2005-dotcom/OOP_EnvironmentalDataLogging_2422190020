from flask import Flask, render_template, request, redirect, url_for
from environment_zone import EnvironmentZone
from measurement import Measurement
from algorithms import zone_statistics
from alert_system import AlertSystem
from trend_prediction import moving_average, predict_next
import random

app = Flask(__name__)

# Alert System
alerts = AlertSystem()

# Create Multiple Zones
zones = {
    "Zone A": EnvironmentZone("Zone A"),
    "Zone B": EnvironmentZone("Zone B"),
    "Zone C": EnvironmentZone("Zone C")
}


# Generate Random Data for a Zone
def generate_data(zone):
    zone.measurements = []
    for i in range(8):
        value = random.uniform(10, 60)
        m = Measurement("S1", value, zone.name)
        zone.add_measurement(m)


# Generate Initial Data
for z in zones.values():
    generate_data(z)


@app.route("/", methods=["GET"])
def home():
    # Selected zone
    zone_name = request.args.get("zone", "Zone A")
    zone = zones[zone_name]

    values = zone.get_values()

    # Statistics
    stats = zone_statistics(zone)
    if stats is None:
        stats = {"min": 0, "max": 0, "mean": 0}

    # Alerts
    alert_messages = []
    for v in values:
        alert = alerts.check_alert("temperature", v)
        if alert:
            alert_messages.append(alert)

    # Trend + Prediction
    trend = moving_average(values)
    prediction = predict_next(values)

    return render_template(
        "index.html",
        zones=list(zones.keys()),
        selected_zone=zone_name,
        zone=zone,
        stats=stats,
        measurements=zone.measurements,
        alerts=alert_messages,
        trend=trend,
        prediction=prediction
    )


@app.route("/generate", methods=["POST"])
def regenerate():
    zone_name = request.form.get("zone")
    zone = zones[zone_name]

    generate_data(zone)

    return redirect(url_for("home", zone=zone_name))


if __name__ == "__main__":
    app.run(debug=True)
