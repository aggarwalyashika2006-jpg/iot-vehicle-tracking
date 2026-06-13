from math import radians
from math import sin
from math import cos
from math import sqrt
from math import atan2

SAFE_LAT = 28.6139
SAFE_LON = 77.2090

def calculate_distance(lat, lon):

    R = 6371

    lat1 = radians(SAFE_LAT)
    lon1 = radians(SAFE_LON)

    lat2 = radians(lat)
    lon2 = radians(lon)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        sin(dlat / 2) ** 2
        +
        cos(lat1)
        * cos(lat2)
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return round(distance, 3)