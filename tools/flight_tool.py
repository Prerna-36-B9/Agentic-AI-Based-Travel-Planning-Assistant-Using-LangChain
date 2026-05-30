import json
import re


def load_flights():
    """
    Load flight data from JSON file.
    """
    with open("datasets/flights.json", "r", encoding="utf-8") as file:
        return json.load(file)


def search_flights(route):
    """
    Search for the cheapest flight between two cities.

    Examples:
    - Mumbai to Goa
    - Cheapest flight from Mumbai to Goa
    - Mumbai to Goa trip
    - Plan a trip from Delhi to Kolkata
    """

    try:

        flights = load_flights()

        route = route.lower().strip()

        # Extract city names
        match = re.search(
            r"([a-zA-Z\s]+)\s+to\s+([a-zA-Z\s]+)",
            route
        )

        if not match:
            return "Please enter route like: Delhi to Goa"

        from_city = match.group(1).strip()

        to_city = match.group(2).strip()

        # Remove extra words after destination
        stop_words = [
            "trip",
            "days",
            "day",
            "budget",
            "travel",
            "vacation",
            "tour",
            "plan"
        ]

        for word in stop_words:
            to_city = re.sub(
                rf"\b{word}\b.*",
                "",
                to_city
            ).strip()

        from_city = from_city.title()
        to_city = to_city.title()

        # Find matching flights
        filtered_flights = [
            flight
            for flight in flights
            if flight["from"].lower() == from_city.lower()
            and flight["to"].lower() == to_city.lower()
        ]

        if not filtered_flights:
            return f"No flights found from {from_city} to {to_city}."

        # Sort by cheapest price
        filtered_flights.sort(key=lambda x: x["price"])

        cheapest_flight = filtered_flights[0]

        return (
            f"✈ Cheapest Flight\n\n"
            f"Airline: {cheapest_flight['airline']}\n"
            f"Price: ₹{cheapest_flight['price']}\n"
            f"Departure: {cheapest_flight['departure_time']}\n"
            f"Arrival: {cheapest_flight['arrival_time']}"
        )

    except FileNotFoundError:
        return "Flights dataset not found."

    except json.JSONDecodeError:
        return "Invalid JSON format in flights dataset."

    except Exception as e:
        return f"Flight Tool Error: {str(e)}"