"""
Madlibs.py

This program prompts the user for words, then prints a story with the words.

Author: Loisa 

"""

print ("Madlibs is starting...")

user_name = input("Enter a name: ")

adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter an adjective: ")
adjective3 = input("Enter an adjective: ")

verb = input("Enter a verb: ")

noun1 = input("Enter a noun: ")
noun2 = input("Enter a noun: ")

animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Entera fruit: ")
superhero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")

# The template for the story
print ("This morning %s " % (user_name.upper()) + "woke up feeling %s. " % (adjective1.upper()) + "It was going to be a %s day! " % (adjective2.upper()) + "Outside, a bunch of %ss were protesting " % (animal.upper()) + "to keep %s in stores. " % (food.upper()) + "They began to %s " % (verb.upper()) + "to the rhythm of the %ss, " % (noun1.upper()) + "which made all the %ss " % (fruit.upper()) + "very %s. " % (adjective3.upper()) + "Concerned, %s " % (user_name.upper()) + "texted %s, " % (superhero.upper()) + "who flew %s " % (user_name.upper()) + "to %s and dropped " % (country.upper()) + "%s in a puddle of frozen " % (user_name.upper()) + "%s. " % (dessert.upper()) + "%s woke up " % (user_name.upper()) + "in the year %s, " % (year) + "in a world where %ss ruled the world." % (noun2.upper()))