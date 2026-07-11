class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.10
        return base_fare + maintenance_charge
my_bus = Bus(capacity=50)
final_fare = my_bus.fare()
print(f"Total Bus Fare: INR {final_fare}")