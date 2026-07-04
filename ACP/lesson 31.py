class Dog:
    animal = "Dog"

    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

dog1 = Dog("Labrador", "Golden")
dog2 = Dog("German Shepherd", "Black and Tan")

print(f"Animal: {dog1.animal}")
print(f"Breed: {dog1.breed}")
print(f"Colour: {dog1.colour}")

print("-" * 20)

print(f"Animal: {dog2.animal}")
print(f"Breed: {dog2.breed}")
print(f"Colour: {dog2.colour}")