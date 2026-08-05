'''class Animal:#Grand parent class
    def Eat(self):
        print("Animal Eats")

class Dog(Animal): #Dog -> inherites the property from Animal of eat PARENT CLASS
    def Bark(self):
        print("Dogs Barks")
        
class Babydog(Dog):#Child class Inherits fronm the parent class of DOG
    def Cry(self):
        print("Baby Dog Cries")
        
a = Babydog()
a.Cry()
a.Bark()
a.Eat()  
'''

class Intern:
    def Fresher(self):
        print("Learning")

class JuniorDev(Intern):
    def Juniordeveloper(self):
        print("Practicing")
        
class SeniorDev(JuniorDev):
    def Seniordeveloper(self):
        print("Teaching")

a = SeniorDev()
a.Fresher()
a.Juniordeveloper()
a.Seniordeveloper()