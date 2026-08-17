class Test :
    @staticmethod
    def add():
        print("I'm Static Method ")
    @staticmethod
    def Mul(a,b):
        print("Mul is : ", a * b)

Test.add()
Test.Mul(10,20)