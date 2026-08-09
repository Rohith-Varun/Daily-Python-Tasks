class Test:
    def M1(self):
        x=10
        print("Value of x is :",x)
t = Test()
t.M1()
#print(t.x) error because x is local variable and it is not accessible outside the method
print(t.M1())
#print(x)