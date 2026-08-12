'''#right angled triangle pattern
for i in range (0,5):#outer Loop
    for j in range (1, i+1):#inner Loop
        print("*",end=" ")
    print("*")
 #explination 
print("-------------------------------------------------------------------------------------------")

#reverse right angled triangle pattern
for i in range (5,0,-1):#outer Loop
    for j in range (1, i+0):#inner Loop
        print("*",end=" ")
    print("*")
 #explination 

print("-------------------------------------------------------------------------------------------")

#left angled triangle pattern
for i in range(0,5):#outer Loop
    for j in range (1, 5-i):#inner Loop
        print(" ",end=" ")
    for k in range (1, i+1):#inner Loop
        print("*",end=" ")
    print("*")
 #explination 

print("-------------------------------------------------------------------------------------------")

#reverse left angled triangle pattern
for i in range(5,0,-1):#outer Loop
    for j in range (0, 5-i):#inner Loop
        print(" ",end=" ")
    for k in range (1, i+0):#inner Loop
        print("*",end=" ")
    print("*")
 #explination 
