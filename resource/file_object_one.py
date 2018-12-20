# This program creates and writes to a textfile.

file_object = open("/home/freedom/Desktop/Python/Files/greetings.txt", "w") # This is how you create a file; by specifying its creation location, then detailing the action that shall be performed of it.

file_object.write("Hello world! Good morning!") # This is how you perform the action that wass earlier detailed (writing on the file).
file_object.close() # You muxt always close the file after creating and writing on it.

say_hi = "import_modules.greetings()"

file_object = open("/home/freedom/Desktop/Python/Files/say_hi.txt", "w")
file_object.write(say_hi)
file_object.close()