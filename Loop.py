import random
"""
# For loop
for i in range(10):
  print(i)
  
for i in range(0, 10, 2):
  print(i)
  
  
  
List = ["apple", "banana", "cherry"]

for i in range(len(List)):
    print(List[i])
    
for i in List:
  print(i) 
  
"""


#While
"""
i=0
while (i < 10):
    print(i)
    i=i+1
"""    
"""
i=0
while True:
    print(i)
    if(i>10):
        break
    else:
        i=i+1
"""
        
RandVal = random.randint(1, 10)       
cnt =0 
while True:
    InVal = input("Please input the number:\n")
    InVal = int(InVal)
    if(InVal == RandVal):
        print("Correct!! the numner is : " + str(RandVal))   
        print(str(cnt) + " Attemps")
        break
    elif(InVal > RandVal):
        print("Too high")
        cnt =cnt+1
    elif(InVal < RandVal):
        print("Too low")
        cnt =cnt+1