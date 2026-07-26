a = int(input("a : "))
b = int(input("b : "))
print(a+b)
print(a-b)
print(a*b)
try:
    print(a/b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    

l=[1,2,3,4]
print(l[2])
try:
    print(l[4]) #IndexError: list index out of range
except IndexError:
    print("Error: Index is out of range.")
print(l[-1])

