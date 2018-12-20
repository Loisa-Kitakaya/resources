# Format for the while loop.

num = 10
condition = 1

while condition <= num:
	print("%d: " % (condition) + "Hello World!")
	condition = condition + 1

# Itegrating the input function to the while loop.

number = 10 
repeat = 0
color = ["white"]

while repeat <= number:
	add_color = input("Enter a color: ")
	color.append(add_color)

	repeat = repeat + 1
print(color)