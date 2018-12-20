# firs imprt the file
# then from the file import the class
# after importing class make object that can use the methods in the class.

# NOTE: After importing the file and then the class within the file (imagine that the class has physically moved into this file and you can see it). Then create an object from the class and now you can call a method with the object.

import class_import_test
import example_class

from class_import_test import importTest
from example_class import exampleClass

ver = importTest() # here is where you make object from the class, that will use the methods in the class.

ver.test("Loisa") # here is where you use the object to call the method in the class importTest.

ver2 = ver.test("Loisa") #here you assign the method to a variable then print the variable.

print (ver2)

ver3 = exampleClass()

ver3.thisMethod()