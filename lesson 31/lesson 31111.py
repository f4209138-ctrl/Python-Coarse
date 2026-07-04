class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed= max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass
School_bus=Bus("school volvo",180,12)
print("Vehicle name:",School_bus.name, School_bus.max_speed, School_bus.mileage)