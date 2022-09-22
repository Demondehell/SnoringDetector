
TestFlg= False

def SayHello():
    print("Hello world!!!")
    (SayHello, 12)
    
def NameSayHello(Name):
    print("Hello " + Name)
    
def Summation(a, b):
    return int(a)+int(b)

def Funct():
    #global TestFlg
    TestFlg = True

def Funct2():
    return True

SayHello()
"""
InputName = input("Please input your name:\n")
NameSayHello(InputName)

value1 = input("Please insert first value:\n")
value2 = input("Please insert second value:\n")
Ans =Summation(value1,value2)
print("The answer is :" + str(Ans))



print(TestFlg)
Funct()
print(TestFlg)

TestFlg = Funct2()
print(TestFlg)
"""