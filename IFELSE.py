import random
#IF else
RandVal = random.randint(1, 10)

"""
InVal = input("Please input the number:\n")
InVal = int(InVal)
if(InVal == RandVal):
    print("Correct")
else:
    print("Not correct")
    
print("The numner is : " + str(RandVal))    
"""

#IF ElseIF
InVal = input("Please input the number:\n")
InVal = int(InVal)
if(InVal == RandVal):
    print("Correct")
elif(InVal > RandVal):
    print("Too high")
elif(InVal < RandVal):
    print("Too low")
    
print("The numner is : " + str(RandVal))   