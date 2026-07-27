import enu
#print(enu.message())
print(enu.message("Hii Varun!, How are you?"))


#2nd way of module creation 
from enu import message
print(message("Hii Varun!, This is the second way of module creation"))

#3rd way of module creation
from enu import message as msg
print(msg("Hii Varun!, This is the third way of module creation"))

#mini calculator
from enu import add
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(add(a, b))

from enu import sub
c = int(input("Enter c : "))
d = int(input("Enter d : "))
print(sub(c, d))

from enu import mul
e = int(input("Enter e : "))
f = int(input("Enter f : "))
print(mul(e, f))

from enu import div
g = int(input("Enter g : "))
h = int(input("Enter h : "))
print(div(g, h))

from enu import add, sub, mul, div
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter c : "))
d = int(input("Enter d : "))
e = int(input("Enter e : "))
f = int(input("Enter f : "))
g = int(input("Enter g : "))
h = int(input("Enter h : "))
print("The sum of two numbers is: ", add(a, b))
print("C - d : ", sub(c, d))
print("e * f : ", mul(e, f))
print("g / h : ", div(g, h))
