# This program is an implementation of the class function to find information about users, using objects.

class physicalFeatures: # Here we create a class "physicalFeatures".

# With the def keywords we define/create methods, i.e. printEyes, printHeight, printWeight, and printHair.


	def printEyes(self): 
		eyes = input("Enter your eye color: ")
		print ("Your eye color is: " + eyes)

		return 0

	def printHeight(self):
		height = input("Enter your height: ")
		print ("Your height is: " + height)

		return 0

	def printWeight(self):
		weight = input("Enter your weight: ")
		print ("Your weight is:" + weight)

		return 0

	def printHair(self):
		hair = input("Enter your hair color: ")
		print ("Your hair is: " + hair)

		return 0

Loisa = physicalFeatures() # Here we create an object "Loisa" which inherits the data of class "physicalFeatures".

print ("Type y for YES and n for NO.")
print ("\n")


print ("Do you want to print your eye color?")
answer = input("y/n: ")
print ("\n")

if answer == "y":
	Loisa.printEyes() # Using the object to call method "printEyes".
	print ("\n")
elif answer == "n":
	print ("Ok! we shall skip that...")
	print ("\n")

print ("Do you want to print your height?")
answer = input("y/n: ")
print ("\n")

if answer == "y":
	Loisa.printHeight() # Using the object to call method "printHeight".
	print ("\n")
elif answer == "n":
	print ("Ok! we shall skip that...")
	print ("\n")

print ("Do you want to print your weight?")
answer = input("y/n: ")
print ("\n")

if answer == "y":
	Loisa.printWeight() # Using the object to call method "printWeight".
	print ("\n")
elif answer == "n":
	print ("Ok! we shall skip that...")
	print ("\n")

print ("Do you want to print your hair?")
answer = input("y/n: ")
print ("\n")

if answer == "y":
	Loisa.printHair() # Using the object to call method "printHair".
	print ("\n")
elif answer == "n":
	print ("Ok! we shall skip that...")
	print ("\n")