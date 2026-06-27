class Parrot:
    species="bird"
    def __init__(self,name,age):
        self.name= name
        self.age= age
p1=Parrot("Blue",3)
p2=Parrot("Woo",5)
print(Parrot.species)
print(f"{p1.name}his age is{p1.age}")

