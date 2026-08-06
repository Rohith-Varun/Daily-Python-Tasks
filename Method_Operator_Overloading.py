class Point:
    def __init__(self, x):
        self.x = x
    
    def __str__(self):
        return str(self.x)
    def __add__ (self, other):
        #return self.x + other.x #only used for the 2 operators 
        return Point(self.x + other.x) #this is used for multiple operators(more than 2)
    
p1 = Point(5)
print(p1)

p2 = Point(4)
print(p2)

p3 = Point(6)
print(p3)
print(p1+p2)
print(p1+p2+p3)