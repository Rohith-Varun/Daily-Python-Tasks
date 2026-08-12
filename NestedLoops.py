print("-------------------------------------------------------------------------------------------")
    
    #rombous pattern
for i in range(0,5):#outer Loop
    for j in range (1, 5-i):#inner Loop
        print(" ",end=" ")
    for k in range (1, i+1):#inner Loop
        print("*",end=" ")
    for l in range (1, i+0):#inner Loop
        print("*",end=" ")
    print("*")
 #explination 

print("-------------------------------------------------------------------------------------------")

#printing of numbers 
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
 #explination 

print("-------------------------------------------------------------------------------------------")

#printing of numbers in rows and columns
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()
 #explination

print("-------------------------------------------------------------------------------------------")

#printing of numbers in square pattern
for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")
    print()
 #explination


print("-------------------------------------------------------------------------------------------")

#hallo squre pattern
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range (0,5):#outer Loop
    for j in range (1, i+1):#inner Loop
        print("*",end=" ")
    print("*")
    for j in range (1, 5-i):#inner Loop
        print(" ",end=" ")
    for k in range (1, i+1):#inner Loop
        print("*",end=" ")
    print("*")

n=int(input(" VAL: "))
for i in range(1,n+1):
    for j in range(i):
        print("*")
