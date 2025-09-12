class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("This is the student constructor"+ self.name)



    def savestudent(self):
        print(self.name+"student details has been saved")