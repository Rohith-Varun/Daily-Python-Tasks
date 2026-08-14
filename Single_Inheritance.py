class Animal():
    def Sound(self):
        print("Animals Makes Sounds")  
class Dog(Animal):
    def Bark(self):
        print("Dog is Barking")
a = Animal()
a.Sound()
a.Bark
d = Dog()
d.Bark()
d.Sound()
