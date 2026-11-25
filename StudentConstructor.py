class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Student Name: ",self.name)
        print("Student Age: ",self.age)

s1 = Student("Sharmada",19)
s1.display()
