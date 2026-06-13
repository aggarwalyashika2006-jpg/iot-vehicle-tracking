import random
from datetime import datetime

SAFE_LAT = 28.6139
SAFE_LON = 77.2090

def generate_location():

    movement_type = random.choice([
        "NORMAL",
        "NORMAL",
        "NORMAL",
        "PARKED",
        "THEFT"
    ])

    if movement_type == "PARKED":

        lat = SAFE_LAT
        lon = SAFE_LON

    elif movement_type == "THEFT":

        lat = SAFE_LAT + random.uniform(0.02, 0.05)
        lon = SAFE_LON + random.uniform(0.02, 0.05)

    else:

        lat = SAFE_LAT + random.uniform(-0.008, 0.008)
        lon = SAFE_LON + random.uniform(-0.008, 0.008)

    return {
        "timestamp": str(datetime.now()),
        "latitude": round(lat, 6),
        "longitude": round(lon, 6),
        "movement_type": movement_type
    }