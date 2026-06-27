class Parrot:
    species="bird"
    def __init__(self,name,age):
        self.name= name
        self.age= age
p1=Parrot("Blue",3)
p2=Parrot("Woo",5)
print(Parrot.species)
print("{} is {} years old".format(p1.name,p1.age))
print("{} is {} years old".format(p2.name,p2.age))

