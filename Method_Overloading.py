#method over riding same name and different parameters 

'''class Test:
    def m1(self):
        print("No arguments menthos")
        
    def m1(self,a):
        print("method with one argument")
        
    def m1(self,a,b):
        print("method with two args")

t = Test()
t.m1("k", "l")
#default args,"args
'''

#method overloading using variable length arguments 
'''class Test():
    def add(self, *l):
        print(sum(l))
        
t = Test()
t.add(10,20)
t.add(10,20,30)
t.add(10,20,30,40)'''

#by using default length arguments 
class Test():
    def add(self, a = 0, b = 0, c = 0):
        print(a+b+c)
 
t = Test()
t.add(10)
t.add(10,20)
t.add(10,20,30)