SAFE_LAT = 28.6139
SAFE_LON = 77.2090

GEOFENCE_RADIUS = 0.01

def is_inside_geofence(lat, lon):

    lat_check = abs(lat - SAFE_LAT)
    lon_check = abs(lon - SAFE_LON)

    if lat_check <= GEOFENCE_RADIUS and lon_check <= GEOFENCE_RADIUS:
        return True

    return False