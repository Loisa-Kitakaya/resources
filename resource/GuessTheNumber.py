"""
The Goal: Similar to the first project, this project also uses the random module in Python. The program will first randomly generate a number unknown to the user. The user needs to guess what that number is. (In other words, the user needs to be able to input information.) If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear. You’ll need functions to check if the user input is an actual number, to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.
Concepts to keep in mind:

Random function
Variables
Integers
Input/Output
Print
While loops
If/Else statements"""

# This program is of a small arithmetic game where the user guesses a number and if the guess is incorrect the user is given hints until the correct answer is established.

import random # here we import the module random so that we can generate our random number.
import author # here we import the module author so that we can be able to display the name of the author of this program.

print ("\n")
author.signature() # calling the attribute signature from module author to display the name of the author.
print ("\n")

number = random.randint(0, 100) # here we use method randint to generate a random number between 0-100 and store the number in varible number.

print ("A number (between 0 and 100) has been generated by the game, can you guess what the number is? \n")
#print (number)

while 1: # a while loop to control the guessing for the random number.

	user_guess = input("Type your guess: ")
	guess = int(user_guess) # converting the user input into intager.

	if guess > number: # if function used to check for the correctness of the guess vs the number generated.

		print ("Your guess is higher than the generated number. \n")

		continue

	elif guess < number:

		print ("Your guess is lower than the generated number. \n")

		continue

	elif guess == number:

		print ("You have guessed correct! Congratulations! \n")
		print ("Now exiting the game...")

		break

	else:

		print ("Please unter a number... (an intager)! \n")

		continue


