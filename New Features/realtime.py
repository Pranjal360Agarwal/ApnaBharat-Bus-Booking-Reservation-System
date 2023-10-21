import random
import time

class Bus:
    def __init__(self, bus_id, route, total_seats):
        self.bus_id = bus_id
        self.route = route
        self.total_seats = total_seats
        self.current_location = 0

    def move_bus(self):
        # Simulate bus movement along the route
        if self.current_location < len(self.route) - 1:
            self.current_location += 1

    def get_location(self):
        return self.route[self.current_location]

def track_bus(bus, interval=5):
    while True:
        bus.move_bus()
        current_location = bus.get_location()
        print(f"Bus {bus.bus_id} is currently at {current_location}")
        time.sleep(interval)

# Example usage:
bus_route = ["City A", "City B", "City C", "City D"]
bus1 = Bus(bus_id=1, route=bus_route, total_seats=30)

# Start tracking the bus in real-time
track_bus(bus1)
