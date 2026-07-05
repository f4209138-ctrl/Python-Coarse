class Point:
    def __init__(self,x,y):
        self.x =x
        self.y =y
    def get_cordinates(self):
        return f"Point({self.x},{self.y})"
p =Point(5,10)
print(p.get_cordinates())