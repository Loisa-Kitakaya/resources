#!/usr/bin/env

# Format for the continue statement that is used in for and while loops.

# Using the continue statement with intagers.

for x in range(1, 21):
	num = x % 2

	if num != 0:
		continue # takes the flow back to the beginning.

	print(x)

# Using the continue statement with strings.
# will also include while, for and if functions.

animals = ["lion", "antlope", "stag", "wolf", "gragon", "trout"]
print(animals)


repeat = 3 # a varible that will control the while loop.
number = 1 # another variable that will control the while loop.
bad_animals = [] # a list that will be initialized by the user and values stored inside.

while number <= repeat:
	choose_animals = input("Enter an animals you don't like from the above list: ")
	bad_animals.append(choose_animals) # the append function adds the user values into the list "bad_animals".

	number = number + 1

	if bad_animals == animals: # the if function compares the contents of both lists.
		continue # takes the flow of the loop back to the beginnig.
print("Animals you don't like: ")
print(bad_animals)