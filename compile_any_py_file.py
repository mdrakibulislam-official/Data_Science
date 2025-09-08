import os
import py_compile

#If we compile py file in the same directory
path = os.getcwd() # get the currrent working directory
fileName = 'py_file_name' #set your desire python file name here
filePath = os.path.join(path, fileName)

#If we need to set the py file with it path, the we will use below line of code 
filePath ="Your python file path"

print(filePath)
py_compile.compile(filePath)
