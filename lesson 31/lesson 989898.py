class Person:
    def __init__(self,name,id_number):
        self.name = name
        self.id_number = id_number
    def display(self):
        print("Name:",self.name)
        print("Id number: ",self.id_number)
class Employee(Person):
    def __init__(self,name,id_number,salary,post):
        super().__init__(name,id_number)
        self.salary = salary
        self.id_number = id_number
        self.post = post
emp = Employee("Jhon","E1042",75000,"Teacher")
emp.display()


