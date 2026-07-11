class BMW:
    def fuel_type(self):
        return "Diesel or Electric"

    def max_speed(self):
        return "250 km/h"

class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "340 km/h"

def car_details(car_object):
    print(f"Fuel Type: {car_object.fuel_type()}")
    print(f"Max Speed: {car_object.max_speed()}")
   
bmw_car = BMW()
ferrari_car = Ferrari()

car_details(bmw_car)
car_details(ferrari_car)