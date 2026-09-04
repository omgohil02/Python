#Classes in python 

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        return f"{self.name} says Woof!"
    
#creating instance

my_dog = Dog("tom",4)   
print(my_dog.bark())  # tom says Woof!    