#Instance Methods
class Student:
    collegename = "CRRCOE"
    def __init__(self):
        self.name = "Varun"
        self.age = 21
        self.dept = "CSE"  
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.dept)
        print("College Name:", Student.collegename)
s1 = Student()
s1.display()
