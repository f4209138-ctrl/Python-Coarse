from abc import ABC, abstractmethod
class Abaclass(ABC):
    def print(self,x):
        print("Passed value: ",x)
    @abstractmethod
    def task(self):
        print(" Inside abstract class")
class test_class(Abaclass):
    def task(self):
        print(" Inside test")
test_obj=test_class()
test_obj.task()
test_obj.print(100)
