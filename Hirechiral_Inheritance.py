'''class Animal:
    def Allanimals(self):
        print("Animals are different")
        
class Dog(Animal):
    def Dogs(self):
        print("Dog is a Animal")
    
class Cat(Animal):
    def Cats(self):
        print("Cat is a Animal")
    
a = Cat() #object creation for the Class Cat
b = Dog() #object creation for the Class Dog
a.Allanimals()
a.Cats()
b.Allanimals()
b.Dogs()'''

class Clg:
    def Dept(self):
        print(" Many Depts")
        
class Cse(Clg):
    def CseDept(self):
        print("Dept of CSE")
    
class IT(Clg):
    def ITDept(self):
        print("Dept of IT")
        
class ECE(Clg):
    def ECEDept(self):
        print("Dept of ECE")
        
class Mech(Clg):
     def MechDept(self):
         print("Dept of Mech")
        
a = Cse()
#b = IT()
#c = ECE()
#d = Mech()
a.Dept()
a.CseDept()

b = IT()
b.Dept()
b.ITDept()

c = ECE()
c.Dept()
c.ECEDept()

d = Mech()
d.Dept()
d.MechDept()
