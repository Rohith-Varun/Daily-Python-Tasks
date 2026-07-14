#arthimetic operators
print("Arthimetic_Operators:")
#addition_operator
a=10
b=10
print(a+b)

#subration_operator
a=20
b=10
print(a-b)

#multiplication_operator
a=10
b=10
print(a*b)

#modulas_operaatior it gives the remainder after the division
a=22
b=7
print(a%b)

#float division // gives the value
a=10
b=5
print(a//b)

#float multiplication ** gives the value
a= 10
b=10
print(a*b)

#division_operator
a=10
b=5
print(a/b)

print("----------------------------------------------------------------------------------------------------------------------")

#Assignment_Operaators
print("Assignment_Operaators:")
a=10
a=10 #= ->assignment
a+=10 #a = a + 10
print(a)

a -=5 #a = a -5
print(a)

a *= 3 #a = a
a *= 3 #a = a *3
print(a)

a %= 10 #a = a %10
print(a)

a /= 2 #a=a/2
print(a)

a =10
a //=5
print(a)

a**=3 #a=a**3
print(a)

print("----------------------------------------------------------------------------------------------------------------------")

#Comparision_Operators
print("Comparision_Operators:")
a=10
b=10
print(a==b) #comparision of values
print(a!=b)

a=10
b=20
print(a==b)
print(a!=b) #not_equal comparision

print(a<b)#greaterthan
print(a>b)#greater
print(a<=b)#lessthan or equal
print(a>=b)#greater or equal

print("----------------------------------------------------------------------------------------------------------------------")

#Logical_Operators
print("Logical_Operators:")
print(10>5 and 10<5)#and

print(10>5 or 10<5)#or

print(not True)#not

print(not False)

print("----------------------------------------------------------------------------------------------------------------------")

#identity operators
print("Identity_Operators:")
a = 10
b = 20
print(id(a))
print(id(b))

print(a is b) #this is mainly used for the comparision of the addresses
print(a == b)

print(a is not b)

#case2:
a=10
b=10
print(id(a))
print(id(b))

print(a is b)
print(a == b)

print(a is not b)

#-5 to 256 -->same address
a=-4
b=-4
print(a is b)

#case3:
a = [1,2,3]
b = [1,2,3]
print(a == b)
#output is true because the values are same
 
print(a is b)
#output is false because the values are same but the address changes because the values are stored in the list 

print(a is not b)
#output is True because the values are same but the address changes because the values are stored in the list 

print("----------------------------------------------------------------------------------------------------------------------")

#Membership_Operaators
print("Membership_Operators:")
a = [10,20,30,40,50,60,70,80,90]#list

print(10 in a)
print(20 not in a)

print(5 in a)
print(15 not in a)

a=(10,20,30,40,50,60,70,80,90)#tuple

print(10 in a)
print(20 not in a)

print(5 in a)
print(15 not in a)


print("----------------------------------------------------------------------------------------------------------------------")

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
print("The value of a+b is : ", a+b)
print("The value of a-b is : ", a-b)
print("The value of a*b is : ", a*b)
print("The value of a/b is : ", a/b)
print("The value of a//b is : ", a//b)
print("The value of a%b is : ", a%b)
print("The value of a**b is : ", a**b)

print("----------------------------------------------------------------------------------------------------------------------")

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
print("The value of a==b is : ", a==b)
print("The value of a!=b is : ", a!=b)
print("The value of a>b is : ", a>b)
print("The value of a<b is : ", a<b)
print("The value of a>=b is : ", a>=b)
print("The value of a<=b is : ", a<=b)