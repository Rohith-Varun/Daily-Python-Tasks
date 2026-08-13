#syntax for creating a class
class MyClass:
    x = 5

#syntax for creating an object of a class
p1 = MyClass()

#syntax for accessing the class attributes
print(p1.x)

#syntax for accessing the class using the object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    