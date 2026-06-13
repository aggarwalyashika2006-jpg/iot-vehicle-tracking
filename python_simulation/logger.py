import csv
import os

FILE_NAME = "data/location_log.csv"

def save_log(data):

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Timestamp",
                "Latitude",
                "Longitude",
                "Distance(km)",
                "Status",
                "Alert",
                "Google Maps"
            ])

        writer.writerow([
            data["timestamp"],
            data["latitude"],
            data["longitude"],
            data["distance"],
            data["status"],
            data["alert"],
            data["maps_link"]
        ])