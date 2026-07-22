#import math
print(math.sqrt(6))
print(int(math.sqrt(6)))
print(math.isqrt(6))

print(math.factorial(5))
print(math.factorial(9))

'''print(math.pi)
print(math.floor(6.5))
print(math.floor(6))
print(round(3.4)) #round is not a math module function to use round we can use round() function directly'''

'''print(math.ceil(3.3))
print(math.ceil(3.5))
print(math.ceil(3.7))
#in the ceil function the value represents the next round of the int value only 
print(math.ceil(2.5))'''

'''print(math.ceil(2.3))#3
print(math.ceil(2.1))#3
print(math.ceil(2.0))#2
print(round(2.2))#2
print(round(2.5))#2
print(round(2.7))#3
#in the ceil fun the value after the point only zero will be considered and print the least value or else it returns the Next int value
#in the round fun the nearset value of the int will return if ,value is <= 5 the below val and >5 the next int val

print(math.pow(3,3))
print(math.pow(5,7))'''
'''
#random - used to generate the raandom values like otps and others fun used is randint
import random
print(random.randint(1000, 9999))'''

'''import random
for i in range(1,5):
    print(random.randint(1,9), end = "")
    
print(random.choice(["red", "blue", "green", "black", "white", "yellow", "orange", "pink", "purple", "brown"]))'''

#date & time module
#import datetime
'''print("Today date and time is :", datetime.datetime.now())

print("Today's date is : ", datetime.date.today())
print("Today's date is : ", datetime.date.today().strftime("%d/%m/%Y"))
print("Today's date is : ", datetime.date.today().strftime("%d-%m-%Y"))
print("The Time is : ", datetime.datetime.now().strftime("%H:%M:%S"))'''
#print("today fate is : ", datetime.date.today()+datetime.timedelta(days = 2))

#sys module
#import sys
'''print(sys.version)
print(sys.version_info)
print(sys.platform)
print(sys.path)'''

'''l = [1,2,3,4]
t = (1,2,3,4)
print(sys.getsizeof(l))
print(sys.getsizeof(t))'''

#os module
'''import os
print(os.name)
print(os.path)
print(os.getcwd())#current working directory returns the current working file path and name'''

#statistics module
'''import statistics
l = [1,3,5,2,8,8,3,5,3,5]
print(statistics.mean(l))
print(statistics.median(l))
print(statistics.mode(l))'''

#json module - JavaScript Object Notation - used to convert the python data into json format in dictonary format this displays the simple datav
