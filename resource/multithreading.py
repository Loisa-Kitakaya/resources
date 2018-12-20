import threading
import datetime
import random
import time

def check_temp():

	temp = random.uniform(1.0, 20.0)
	time_ = datetime.datetime.now()

	if temp >= 15.0:

		print ("\nToo hot! Opening vents...")

		time.sleep(2.5)

	elif temp <= 5.0:

		print ("\nToo cold! Closing vents...")

		time.sleep(2.5)

	else:

		print ("\nTemp is OK...")

		time.sleep(2.5)

def check_humidity():

	humidity = random.uniform(20.0, 40.0)
	time_ = datetime.datetime.now()

	if humidity >= 35.0:

		print ("\nToo much water in atmosphere! Dehumiditizing...")

		time.sleep(2.5)

	elif humidity <= 25.0:

		print ("\nHumidity back to normal! Stopping dehumiditization...")

		time.sleep(2.5)

	else:

		print ("\nHumidity level is OK...")

		time.sleep(2.5)

def check_soilH2O():

	soilH2O = random.uniform(100.0, 500.0)
	time_ = datetime.datetime.now()

	if soilH2O <= 250.0:

		print ("\nSoil H2O is low! Watering plants...")

		time.sleep(2.5)

	elif soilH2O >= 450.0:

		print ("\nSoil H2O is back to normal! Stopping water flow...")

		time.sleep(2.5)

	else:

		print ("\nSoil H2O is OK...")

		time.sleep(2.5)

def main():

	while True:

		for i in range(10):

			thread_1 = threading.Thread(target = check_temp)
			thread_2 = threading.Thread(target = check_humidity)
			thread_3 = threading.Thread(target = check_soilH2O)

			thread_1.start()
			thread_2.start()
			thread_3.start()

			thread_1.join()
			thread_2.join()
			thread_3.join()

		print ("Done!")

		again = input ("\nshow stats again? [y/n]: ")

		if again == "y":

			continue

		elif again == "n":

			break

main()	