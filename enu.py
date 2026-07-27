def message():
    return "Helloo..!"
print(message())'''

def message(name):
    return "Helloo..! " + name
print(message("Varun! How are you?"))

#mini calculator
def add(a, b):
    return a + b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("The sum of two numbers is: ", add(a, b))

def sub(c,d):
    return c - d
c = int(input("Enter c : "))
d = int(input("Enter d : "))
print("C - d : ", sub(c - d))

def mul(e,f):
    return e * f
e = int(input("Enter e : "))
f = int(input("Enter f : "))
print("e * f : ", mul(e * f))

def div(g,h):
    return g / h
g = int(input("Enter g : "))
h = int(input("Enter h : "))
print("g / h : ", div(g / h))
