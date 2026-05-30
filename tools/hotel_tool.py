import json
import re


def load_hotels():

    with open("datasets/hotels.json", "r", encoding="utf-8") as file:
        return json.load(file)


def recommend_hotels(input_text):

    try:

        hotels = load_hotels()

        city = None

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

        for c in cities:
            if c.lower() in input_text.lower():
                city = c
                break

        if not city:
            return "Please specify a city."

        filtered_hotels = [
            hotel
            for hotel in hotels
            if hotel["city"].lower() == city.lower()
        ]

        if not filtered_hotels:
            return f"No hotels found in {city}."

        # --------------------
        # STAR FILTER
        # --------------------

        star_match = re.search(r"(\d)\s*-?\s*star", input_text.lower())

        if star_match:

            stars = int(star_match.group(1))

            filtered_hotels = [
                hotel
                for hotel in filtered_hotels
                if hotel["stars"] >= stars
            ]

        # --------------------
        # BUDGET FILTER
        # --------------------

        if "budget" in input_text.lower():

            filtered_hotels.sort(
                key=lambda x: x["price_per_night"]
            )

        else:

            filtered_hotels.sort(
                key=lambda x: (
                    -x["stars"],
                    x["price_per_night"]
                )
            )

        top_hotels = filtered_hotels[:5]

        output = f"🏨 Best Hotels in {city}\n\n"

        for hotel in top_hotels:

            output += (
                f"🏨 {hotel['name']}\n"
                f"⭐ Stars: {hotel['stars']}\n"
                f"💰 Price/Night: ₹{hotel['price_per_night']}\n"
                f"✨ Amenities: {', '.join(hotel['amenities'])}\n"
                f"{'-'*35}\n"
            )

        return output

    except Exception as e:

        return f"Hotel tool error: {str(e)}"