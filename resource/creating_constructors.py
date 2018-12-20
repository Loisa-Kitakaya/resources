# This progragam shows how to create a constructor (an automated method), such that you dont have to call a method with an object.

# Note: A constructor (automated method) does not return anything.

class newClass: # Creating the class.
	def __init__ (self): # creating a constructor/automating a method. This is done by the key word "__init__".
		x = 10
		y = 20
		z = x + y

		print ("The sum of 10 and 20 is: ", z)

newObject = newClass()
