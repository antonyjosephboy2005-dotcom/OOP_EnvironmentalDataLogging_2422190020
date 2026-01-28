from flask import Flask, render_template
from src.environment_zone import EnvironmentZone
from src.algorithms import zone_statistics

app = Flask(__name__)

# Example zone data
zone_a = EnvironmentZone("Zone A")
zone_a.measurements = []

@app.route("/")
def home():
    stats = zone_statistics(zone_a)

    return f"""
    <h1>Environmental Monitoring Dashboard</h1>
    <p>Zone: {zone_a.name}</p>
    <p>Statistics: {stats}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
