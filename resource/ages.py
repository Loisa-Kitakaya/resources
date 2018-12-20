# This program will print out the ages of a few people, utilizing the sequence dictionary.

ages = {"Mom" : 45, "Dad" : 47, "Sis" : 19, "Me" : 22}

for item in ages: # This for function prints out only the items in the dictionary and not their values.
	print (item)
	print ("\n")

for item in ages: # This for function prints out both the items in the dictionary and their values.
	print (item, "is", ages[item], "years old.")