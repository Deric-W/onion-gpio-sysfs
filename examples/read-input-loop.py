## EXAMPLE CODE
# Set the GPIO to input, then read and print the value every second

import time
from onionGpio import OnionGpio, Direction


gpioNum = 7
with OnionGpio(gpioNum) as gpioObj:
	# set to input 
	gpioObj.setDirection(Direction.INPUT)

	# read and print the value once a second
	while True:
		print('GPIO%d input value: %s' % (gpioNum, gpioObj.getValue().name))
		time.sleep(1)
