
TestFlg= False


def SayHello():
    print("Hello world")
    
def NameSayHello(Name):
    print("Hello " + Name)
    
def Summation(a, b):
    return int(a)+int(b)

def Funct():
    global TestFlg
    TestFlg = True


SayHello()
InputName = input("Please input your name:\n")
NameSayHello(InputName)

value1 = input("Please insert first value:\n")
value2 = input("Please insert second value:\n")
Ans =Summation(value1,value2)
print("The answer is :" + str(Ans))
print(TestFlg)
Funct()
print(TestFlg)