book = {"mom":"200", "dad":"454"}

print (book)

for info in book:
	print (info)

	print (book[info])

for x in book:
	print ("\t", x, "\t", book[x])

ans = "mom"

pans = "cat"

if ans in book:
	print ("true")

if pans in book:
	print ("true")
else:
	print ("false")