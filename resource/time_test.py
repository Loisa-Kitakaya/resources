import datetime
from datetime import *
import time

now = str(datetime.now())

print (now)

time.sleep(10)

after_sleep = datetime.datetime.now()

delay = after_sleep - now

print (after_sleep)

print (delay)