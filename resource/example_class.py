# This program is to demonstrate how to create a class, an object and how to call them.

class exampleClass: # This is how to you create/define a class (line 3-16)
	name = "Loisa"
	age = 22
	eyes = "black"
	height = 5.6

	def thisMethod(self): # This is normally how you define a function, but within a class, all functions become methods.
		x = 20
		y = 30

		print ("Hello there! How are you doing?")
		print ("\n")

		return (x * y)

Lui = exampleClass() # This is how you create an object; by linking it to a class i.e. feeding the object the data of the class.

print (Lui.name)
print (Lui.age)
print (Lui.eyes)
print (Lui.height)
print ("\n")
print (Lui.thisMethod())