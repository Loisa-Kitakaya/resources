# This is a program to learn how to use a function (user defined).
# The funtion will be used to send sout outs.

def shout_outs (holla): # This user defined function utilizes string data types.
	return ("shout out ma' hommie " + holla + "!") # This statement command the function to return a certain value, a greeting in this example.

print ("Type 'quit' if you've given enough names for shout outs.")
print ("\n")

while 1:
	holla = input("Enter a person to shout out: ")

	if holla == "quit": # An if and break function to break the endless loop.
		print ("Cool!")
		break

	print (shout_outs(holla))

def plus_3k (x): # This user defined function utilizes intager data types.
	return (x + 3000) # this statement commands the function to return a value, an addition in this example.

print ("Type 'quit' if you've given enough names for shout outs.")
print ("\n")

while 1:
	x = input("Enter a number to add: ")

	if x == "quit":
		print ("Aaight!")
		break

	print (plus_3k(int(x))) # Here "int()" converts the input from string to intager so that it is able to be added to 3000.