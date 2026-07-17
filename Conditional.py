a=int(input("Enter : "))
if a%3==0 and a%5==0:
    print("Fizz..Buzz..")
elif a%5==0:
    print("Buzz")
elif a%3==0:
    print("Fizz")
else :
    print("Not Divisible by 3 & 5")
    
print("--------------------------------------------------------------------------------------------------------")

a=int(input("age : "))
if a >=18:
    print("Major")
    if a >= 65:
        print("Senior Citizen")
        if a < 65:
            print("Not SRC")
print("Minor")

a=int(input("Marks : "))
if a >= 35:
    print("Just Passed")
    if a >= 36 and a <=75:
        print("Eligible for Scholarship")
        if a <= 76:
            print("Meret")
else:
    print("Failed")

a = int(input("Enter Pin : "))
if a == 1111:
    print("The Pin Entered Is Correct")
    b= int(input("Enter Amt : "))
    if b > 25000:
        print("Cant WithDraw More AMT")
        if b <= 100:
            print("Invalid Amt")
    else:
        print("Amt Transaction Done...")
else:
    print("Wrong Pin")
    