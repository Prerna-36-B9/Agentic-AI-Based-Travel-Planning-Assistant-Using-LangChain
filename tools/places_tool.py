import json


def load_places():

    with open("datasets/places.json", "r", encoding="utf-8") as file:
        return json.load(file)


def recommend_places(input_text):

    try:

        places = load_places()

        cities = [
            "Delhi",
            "Mumbai",
            "Goa",
            "Bangalore",
            "Chennai",
            "Hyderabad",
            "Kolkata",
            "Jaipur"
        ]

        city = None

        for c in cities:

            if c.lower() in input_text.lower():
                city = c
                break

        if not city:
            return "Please specify a city."

        filtered_places = [
            place
            for place in places
            if place["city"].lower() == city.lower()
        ]

        if not filtered_places:
            return f"No tourist places found in {city}."

        filtered_places.sort(
            key=lambda x: x["rating"],
            reverse=True
        )

        top_places = filtered_places[:5]

        output = f"🌴 Top Tourist Attractions in {city}\n\n"

        for place in top_places:

            output += (
                f"📍 {place['name']}\n"
                f"🏷 Type: {place['type'].title()}\n"
                f"⭐ Rating: {place['rating']}\n"
                f"{'-'*35}\n"
            )

        return output

    except Exception as e:

        return f"Places tool error: {str(e)}"