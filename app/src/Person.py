# Create a new class called Person
# The Person class must have two attribues:
#   1. name (str)
#   2. age (int)
class Person(): #creates new class called person
    def __init__(self, name: str, age: int): #instantiates the class
        self.name = name
        self.age = int(age)