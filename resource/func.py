import random

def light(name, floor):

	print ("%s is open at floor %d" % (name, floor))

def not_light(name, floor):

	print ("%s is open at floor %d" % (name, floor))

def main():

	count1 = 0
	count2 = 0

	while True:

		check = random.randint(1,3)

		if check == 1:

			light("toilet 1", 1)

			count1 += 1

			print ("opened for the %dth time" % (count1))

		elif check == 2:

			not_light("toilet 2", 2)

			count2 += 1

			print ("opened for the %dth time" % (count2))

		else:

			print ("Just hold it in!")

		again = input ("check again? [y/n]: ")

		if again == "y":

			continue

		elif again == "n":

			break

		else:

			print ("Really!")

main()