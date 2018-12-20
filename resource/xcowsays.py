import os

def main():

	print ("Do you want to see your fortune today?!")

	while True:

		ans = input ("\n[y] for 'YES' | [n] for 'NO': ")

		if ans == "y":

			print ("\n")
			os.system("fortune")
			print ("\n")

			break

		elif ans == "n":

			print ("\nI know you will be back! B-)")

			break

		else:

			print ("\nI can already tell your fortune will be bad...")
			print ("\nJust follow the goddamn instructions!")

			continue

main()