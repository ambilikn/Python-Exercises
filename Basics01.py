#Print area of a circle

x = float(input())
print("Input is ",x)
pi = 3.141592653589
area = pi*x*x

#Print extension of a filename

import os
  
  
# this will return a tuple of root and extension
split_tup = os.path.splitext(input())
print(split_tup)
  
# extract the file name and extension
file_name = split_tup[0]
file_extension = split_tup[1]
  
#print("File Name: ", file_name)
print("File Extension: ", file_extension)


if file_extension == ".py":
    print("It is a python file!!")
elif file_extension == ".c":
    print("It is a C file!!")
elif file_extension == ".cpp":
    print("It is a c++ file!!")
elif file_extension == ".txt":
    print("It is a text file!!")
elif file_extension == ".java":
    print("It is a java file!!")
else:
    print("Not sure!!")

