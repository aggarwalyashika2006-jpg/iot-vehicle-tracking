from python_simulation.geofence import is_inside_geofence

def detect_status(lat, lon, movement_type):

    inside = is_inside_geofence(lat, lon)

    if movement_type == "PARKED":
        return "PARKED"

    if not inside:
        return "THEFT SUSPECTED"

    return "MOVING SAFELY"