class Student:
    collegename = "CRRCOE"
    
    def __init__(self):
        self.name = "Varun"
        self.age = 21
        self.dept = "CSE"
s1 = Student()
print(s1.collegename)
print(s1.name)
print(Student.collegename)
s2 = Student()
print(s2.collegename)
