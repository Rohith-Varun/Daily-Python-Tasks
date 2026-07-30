class Student:
    collegename = "CRRCOE"
    @classmethod #@classmethod - this is a decorator which is used to define the class method if not defined then only it becomes the class method and the class variable can be accessed outside the class
    def GetCollegeInfo(cls): #(cls) - this must be mentioned for the class method then only then only the class variable can be accessed outside the class
        print("My clg name is :", cls.collegename) 
print(Student.collegename)
Student.GetCollegeInfo()
