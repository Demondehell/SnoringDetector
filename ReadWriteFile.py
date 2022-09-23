FileName ="D:/Python Training/myfile.txt"


"""
#create File
file1 = open(FileName,"w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]  
# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file access modes
  

#read File
file1 = open(FileName,"r+")  
print("Output of Read function is ")
print(file1.read())
print()



#Append file
# Open a file with access mode 'a'
file1 = open(FileName, 'a')
file1.write("This is Bankok \n")
file1.close()

#read File
file1 = open(FileName,"r+")  
print("Output of Read function is ")
print(file1.read())
print()


"""
# Using readline()
file1 = open(FileName, 'r+')
count = 0
while True:
    line = file1.readline()
    count = count+1
    if not line:
        break
    print("Line{}: {}".format(count, line.strip()))
file1.close()
