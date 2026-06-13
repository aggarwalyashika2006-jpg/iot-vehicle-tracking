import requests

WRITE_API_KEY = "DDFC2ML9CF0KX5Z0"

def upload_data(
    latitude,
    longitude,
    distance,
    status_code
):

    url = "https://api.thingspeak.com/update"

    payload = {
        "api_key": WRITE_API_KEY,
        "field1": latitude,
        "field2": longitude,
        "field3": distance,
        "field4": status_code
    }

    response = requests.get(
        url,
        params=payload
    )

    print(
        "ThingSpeak Response:",
        response.text
    )