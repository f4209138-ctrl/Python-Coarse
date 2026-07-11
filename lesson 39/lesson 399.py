from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class human(Animal):
    def move(self):
        print("I can walk and run")
class snake(Animal):
    def move(self):
        print("I can crawl")
class Dog(Animal):
    def move(self):
        print("I can bark and run")        
human= human()
dog= Dog()
human.move()
snake= snake()
dog.move()
        