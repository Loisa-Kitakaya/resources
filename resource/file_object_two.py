# This program reads from a text file.

file_object = open("/home/freedom/Desktop/Python/Files/greetings.txt", "r") # This is how you read data from a file; first by detailing its location in the memory then, detailing the action to be performed on it, which is reading.
info = file_object.read() # The data is read from the file and stored in the variable info.

print (info) # The value of variable "info" is displayed: this is the data read from the file.

file_object.close()