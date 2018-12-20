# This program append data to a list.

for x in range(0,21):
	dice_roll = input(">>> ")

	record = ["Your rolls: "]
	record_data = str(dice_roll)
		
	record.append(record_data)

	print (record)

face = ["1", "2", 5, 6]

print (face)

number = input(">>> ")

face.append(number)

print (face)