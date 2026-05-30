import re


def estimate_budget(details):

    try:

        # Default values
        days = 3

        # Extract number of days from text
        match = re.search(r"(\d+)\s*-?\s*day", details.lower())

        if match:
            days = int(match.group(1))

        # Cost assumptions
        flight_cost = 5000
        hotel_per_day = 3000
        food_per_day = 1000
        transport_per_day = 500

        hotel_cost = hotel_per_day * days
        food_cost = food_per_day * days
        transport_cost = transport_per_day * days

        total_cost = (
            flight_cost
            + hotel_cost
            + food_cost
            + transport_cost
        )

        return f"""
💰 Budget Estimate

Trip Duration: {days} Days

Flight Cost: ₹{flight_cost}
Hotel Cost: ₹{hotel_cost}
Food Cost: ₹{food_cost}
Transport Cost: ₹{transport_cost}

--------------------------------
Total Estimated Budget: ₹{total_cost}
"""

    except Exception as e:

        return f"Budget Tool Error: {str(e)}"