import requests


CITY_COORDINATES = {
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Goa": (15.2993, 74.1240),
    "Bangalore": (12.9716, 77.5946),
    "Hyderabad": (17.3850, 78.4867),
    "Chennai": (13.0827, 80.2707),
    "Kolkata": (22.5726, 88.3639),
    "Jaipur": (26.9124, 75.7873)
}


def get_weather(input_text):

    try:

        city = None

        for c in CITY_COORDINATES.keys():

            if c.lower() in input_text.lower():
                city = c
                break

        if not city:
            return "Please specify a supported city."

        latitude, longitude = CITY_COORDINATES[city]

        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={latitude}"
            f"&longitude={longitude}"
            f"&current=temperature_2m,weather_code"
            f"&daily=temperature_2m_max,temperature_2m_min"
            f"&timezone=auto"
        )

        response = requests.get(url, timeout=10)

        data = response.json()

        current_temp = data["current"]["temperature_2m"]

        max_temp = data["daily"]["temperature_2m_max"][0]

        min_temp = data["daily"]["temperature_2m_min"][0]

        return f"""
🌦 Live Weather in {city}

🌡 Current Temperature: {current_temp}°C
🔺 Max Temperature: {max_temp}°C
🔻 Min Temperature: {min_temp}°C
"""

    except Exception as e:

        return f"Weather tool error: {str(e)}"