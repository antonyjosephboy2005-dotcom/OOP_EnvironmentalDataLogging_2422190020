def calculate_average(zone):
    values = zone.get_values()
    return sum(values) / len(values) if values else 0


def zone_statistics(zone):
    values = zone.get_values()
    if not values:
        return None

    return {
        "min": min(values),
        "max": max(values),
        "mean": calculate_average(zone)
    }


def sort_zones_by_pollution(zones):
    return sorted(zones, key=lambda z: calculate_average(z), reverse=True)
