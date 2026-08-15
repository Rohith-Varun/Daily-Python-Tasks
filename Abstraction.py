from abc import ABC,abstractmethod
class Mobile(ABC):
    @abstractmethod
    def battery(self): #abstraction method
        pass
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def memory_space(eslf, ram, rom):
        pass
    def details(self): #concreate method cause the method have name and declaration
        return "Hello Nothing"
#we can't create an object to the abstract class because they are temporary 
#m = Mobile() #TypeError: Can't instantiate abstract class Mobile without an implementation for abstract methods 'battery', 'display', 'memory_space'
class Nothing(Mobile): #child class -> this makes all the abstract classes will be abstracted to the child class 
    def __init__ (self, model, display_quality,camera_quality):
        self.model = model
        self.display_quality = display_quality
        self.camera_quality = camera_quality
    def battery(self):
        return f"Nothing have {self.model}, and display {self.display_quality}"
    def display(self):
        return f"Nothing have display_quality {self.display_quality}"
    def memory_space(eslf, ram, rom):
        return f"Nothing have ram {ram}, rom {rom}"
    
n = Nothing("3a 5G", 10000, 1080)
print(n.battery())
print(n.display())
print(n.memory_space(8, 128))
