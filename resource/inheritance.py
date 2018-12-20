# This is a program based on classes and implements inheritance.

class ParentClass: # Creating the class.
	var1 = "I am var one!"
	var2 = "I am var two!"

	def printItems(self):
		var1 = "la la la la..."
		var2 = "goodbye..."

		return var1 + var2

class childClass(ParentClass): # Creating the child class such that it inherits everything from the parent class.
	pass

parentObject = ParentClass() # Creating an object.
childObject = childClass() # Creating an object.

print (parentObject.var1)
print ("\n")
print (parentObject.var2)
print ("\n")

print (childObject.var1)
print ("\n")
print (childObject.var2)
print ("\n")

parentObject.printItems()
childObject.printItems()