class Student:
    collegename = "CRRCOE"
    
    def __init__ (self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def display(self):
        print("My name is : ", self.name)
        print("My age is : ", self.age)
        print("My marks is : ", self.marks)
        
s1 = Student("Varun", 22, 90)
s2 = Student("Rohith", 21, 80)
s1.display()
s2.display()