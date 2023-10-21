import random

def recommend_best_bus(user_preferences, available_buses):
    # Simulated recommendation algorithm
    recommended_bus = random.choice(available_buses)
    return recommended_bus

# Example usage:
user_preferences = {
    "source": "City A",
    "destination": "City B",
    "date_of_travel": "2023-10-25",
    "number_of_tickets": 2,
    # Add more user preferences as needed
}

available_buses = [
    {"bus_name": "Bus X", "price": 50, "available_seats": 20},
    {"bus_name": "Bus Y", "price": 40, "available_seats": 10},
    # Add more bus options
]

recommended_bus = recommend_best_bus(user_preferences, available_buses)

print("Recommended Bus:")
print("Bus Name:", recommended_bus["bus_name"])
print("Price:", recommended_bus["price"])
print("Available Seats:", recommended_bus["available_seats"])
