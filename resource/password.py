# A small program that prompts for the user password, saves it, checks again if the password is correct.

pass_list = []
password = input("Enter your new password: ")
print ("\n") # This will print a blank line (next line).

pass_list.append(password) # This will append/add the input in variable "password" to the sequence list "pass_list".

print ("You will need to confirm your password.")
confirm_password = input("Re-enter your new password: ")
print ("\n")

if confirm_password in password: # This if function checks to see if the new password (confirm_password) is same as the one in list pas_list.
	print ("Yep! That is the correct password.")
else:
	print ("Nope! The password you have entered is not the same one you entered before.")