""" The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice. When the program runs, it will randomly choose a number between 1 and 6. (Or whatever other integer you prefer — the number of sides on the die is up to you.) The program will print what that number is. It should then ask you if you’d like to roll again. For this project, you’ll need to set the min and max number that your dice can produce. For the average die, that means a minimum of 1 and a maximum of 6. You’ll also want a function that randomly grabs a number within that range and prints it.
Concepts to keep in mind:

Random
Integer
Print
While Loops """

import random # here we have imported the random module to generate the random number.
import author # here we have imported the author module to print the author of this program.
import datetime

print ("\n")
author.signature() # here we call the method "signature" which displays the name of the author of this program.

print ("\n")
print ("This program simulates the rolling of die and stores the dice rolls on an external log file. \n")
print ("The location for the log file is: /home/freedom/Desktop/Python/Files/dicerolls.txt \n")

print ("To quit the program, type 'quit' when you are prompted to roll the dice. \n")

while 1: # we use a while loop to the process of rolling the dice infinitely until the user wishes to stop.
	print ("\nDo you want to roll the dice? ['yes' or 'quit']")

	answer = input(">>> ") # the user prompts the program if they want to roll the dice (this process will be repeated until the user wishes to quit).
	print ("\n")

	dice_roll = random.randint(1,6) # here we use the module random and call the "randint" method which generates a random intager, and from our specified values for the method... the intager value is between 1-6. the value is then stored in the variable "dice_roll".

	if answer == "yes": # here we use an if function to control the repeating process that prompts for the rolling of the dice.
	
		print (dice_roll)

	elif answer == "quit":

		print ("Exiting simulation...")

		break

	else:

		print ("Wrong input, try again. \n")

	dice_result = str(dice_roll) #here we convert the randomly generated intager into a string and save it in the variable "dice_result".

date = datetime.datetime.now()
date2 = str(date)

dicerolls = open ("/home/freedom/Documents/Python/logs/dicerolls.txt", "a") # here we create an object that opens a file and writes on it.
dicerolls.writelines("\n")
dicerolls.writelines(date2)
dicerolls.writelines("\tProgram run successfuly\n.")
dicerolls.close() # here we close the file.