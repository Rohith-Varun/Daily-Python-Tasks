'''class Bank:
    def __init__ (self, name, balance, password):
        self.name = name
        self._balance = balance # "_" means protected single underscore means protected variable
        self.__password = password #"__" means private double underscore means private variable
    def m1(self):
        pass
    def m2(self):
        pass
    
t = Bank("Varun", 10000, 1234)
print(t.name)
t.name = "Rohith"
print(t.name)
print(t._balance)
t.__password = 1244
print(t.__password)'''

class Bank:
    def __init__(self, name, balance, password):
        self.name = name
        self._balance = balance
        self.__password = password
    def get_balance(self):
        return self._balance
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            return f"transaction successful, update balance is : {self._balance}"
        else:
            return f"tansation failed"
        
b = Bank("Varun", 5000, 1234)
print(b.name)
print(b._balance)
#print(b.__password) error 
print(b._Bank__password)
print(b.withdraw(2000))