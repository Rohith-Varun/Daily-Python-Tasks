class Student:
    def __init__(self):
        self.name = "Varun"
        self.age = 21
        self.dept = "CSE"
        print("My name is :", self.name)
        print("My age is :", self.age)
        print("My dept is :", self.dept)
s1 = Student()
print(s1.name)
print(s1.age)
print(s1.dept)
print(id(s1))
print(id(s1.name))