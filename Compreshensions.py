l=[i for i in range(1,11)]
print(l)
l = [1,2,3,4,5,6,7,8,9,10]
a = [i for i in l if i%2==0]
print(a)
l = [1,2,3,4,5,6,7,8,9,10]
a= ["Even" if i%2==0 else "Odd" for i in range(1,5)]
print(a)

l = [1,2,3,4,5,6,7,8,9,10]
a= ["Even" if i%2==0 else "Odd" for i in range(1,5)]
print(a)

a=["p", "y", "t", "h", "o", "n"]
for index, value in enumerate(a):
    print(index, value)
