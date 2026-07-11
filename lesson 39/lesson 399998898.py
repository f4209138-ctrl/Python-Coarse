class India():
    def capital(self):
        print("capital=New delhi")
    def language(self):
        print("language = HIndi/English")
    def type(self):
        print("type = devloping country")
class USA():
    def capital(self):
        print("capital=Washington DC")
    def language(self):
        print("language = English")
    def type(self):
        print("type = devloped country")
obj_ind=India()
obj_usa=USA()
for country in(obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()
