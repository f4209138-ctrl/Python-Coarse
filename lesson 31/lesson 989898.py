class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Employee(Person):
    def __init__(self,name,age,employee_id,salary):
        super().__init__(name,age)
        self.salary = salary
        self.employee_id = employee_id
emp = Employee("Jhon","E1042",75000,90983)
emp.display()


