# This program will let the user enter their email address and their passwords, thaen compare their credentials during login. This program shall be implemented using the if function.

email_list = [] # Create a list sequence to store the emails.
pass_list = [] # Create a list sequence to store the passwords.

email = input("Enter your email address: ")
password = input("Enter the password for your email address: ")
print ("\n")

email_list.append(email) # Append the values of "email" to email_list
pass_list.append(password) # Append the values of "password" to pass_list

print ("You now need to login.")
print ("Enter your email and password below.")
print ("\n")

new_email = input("Email: ")
new_password = input("password: ")

if (new_email in email_list) and (new_password in pass_list): # The if function checks that the login details are correct and prints out a message accordingly.
	print ("You are now logged in! Congratulations!")
else:
	print ("Wrong login details.")