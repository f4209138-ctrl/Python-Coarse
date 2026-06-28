class Employee:
    def __init__(self):
        print("Costructor called")
    def __del__(self):
        print("Destructor called")
def manage_employee():
    emp=Employee()
    del emp
manage_employee()