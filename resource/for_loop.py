# Format of the for loop

"""
for <variable> in <sequence>:
	<statement>
else:
	<statement>

 The variable holds the values of the following sequence.

 The items of the sequence object are assigned one after the other to the loop variable; to be precise the variable points to the items. For each item the loop body is executed.

"""

# Testing the for loop 

languages = ["C", "C++", "HTML", "C#", "Java", "Ruby on rails", "Java Script"]

for x in languages:
	print (x)

# Integrating the range funtion into the for loop.
# Also integrating the if function.

num = 10

for counter in range(1, num + 1):
	if counter <= num:
		print("%d: " % (counter) + "Hello world!")

# List iteration (for loop) integrating the input function.

color = ["red"]
n = 5

for x in range(1, n + 1):
	if x <= n:
		add_color = input("Enter a new color: ")
		color.append(add_color) # The append function adds the user input to the list.
print(color)