# Create a class named Student
# The Student class must extend the Person class
# In addition to the Person class attribute, the Student class must have the following attributes:
#   1. id (int)
#   2. grade (float)
from app.src.Person import Person

class Student(Person): #inherit the traits from person and creates the student class
    def __init__(self,name: str, age:int, id: int, grade: float):
        super().__init__(name, age)#this inherits from person
        self.id = int(id) #id
        self.grade = float(grade) #grade