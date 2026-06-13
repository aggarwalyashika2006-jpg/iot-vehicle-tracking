import time

from python_simulation.gps_simulator import generate_location
from python_simulation.distance_calculator import calculate_distance
from python_simulation.theft_detector import detect_status
from python_simulation.logger import save_log
from python_simulation.thingspeak_uploader import upload_data
print("\nVehicle Tracking System Started...\n")

while True:

    vehicle = generate_location()

    distance = calculate_distance(
        vehicle["latitude"],
        vehicle["longitude"]
    )

    status = detect_status(
        vehicle["latitude"],
        vehicle["longitude"],
        vehicle["movement_type"]
    )

    alert = "NONE"

    if status == "THEFT SUSPECTED":
        alert = "GEOFENCE ALERT"

    maps_link = (
        f"https://maps.google.com/?q="
        f"{vehicle['latitude']},"
        f"{vehicle['longitude']}"
    )

    record = {
        "timestamp": vehicle["timestamp"],
        "latitude": vehicle["latitude"],
        "longitude": vehicle["longitude"],
        "distance": distance,
        "status": status,
        "alert": alert,
        "maps_link": maps_link
    }

    save_log(record)
    status_code = 0
    if status == "THEFT SUSPECTED":
        status_code = 1
    upload_data(
        vehicle["latitude"],
        vehicle["longitude"],
        distance,
        status_code
        )

    print("=" * 60)
    print("Time:", vehicle["timestamp"])
    print("Latitude:", vehicle["latitude"])
    print("Longitude:", vehicle["longitude"])
    print("Distance:", distance, "km")
    print("Status:", status)
    print("Alert:", alert)
    print("Maps:", maps_link)

    time.sleep(3)