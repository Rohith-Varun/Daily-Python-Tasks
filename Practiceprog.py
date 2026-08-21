# Example showing Instance Variable, Class Variable, Instance Method, Class Method, and Static Method
class Student:
    school_name = "CRRCOE"  # Class variable

    def __init__(self, name, marks):  # Parameterized constructor
        self.name = name              # Instance variable
        self.marks = marks            # Instance variable

    def display_info(self):     # Instance method
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"School: {self.school_name}")

    @classmethod
    def change_school(cls, new_name):  # Class method
        cls.school_name = new_name
        print(f"School changed to: {cls.school_name}")

    @staticmethod
    def is_pass(marks):  # Static method
        return marks >= 35

# Creating objects
s1 = Student("Rohith", 80)
s2 = Student("Varun", 30)

# Using instance method
s1.display_info()
print()
s2.display_info()

# Using class method
Student.change_school("Python Academy")
print()

# Using static method
print(f"Is Rohith pass? {Student.is_pass(s1.marks)}")
print(f"Is Varun pass? {Student.is_pass(s2.marks)}")
