## EXAMPLE CODE
# Set a GPIO to output, and alternate the output between LOW and HIGH every 5 seconds

import time
from onionGpio import OnionGpio, Value, Direction

gpioNum = 1
with OnionGpio(gpioNum) as gpioObj:
	# set to output 
	gpioObj.setDirection(Direction.OUTPUT_LOW)		# initialize the GPIO to 0 (LOW)

	# alternate the value
	value = Value.LOW
	while True:
		# reverse the value
		if value == Value.LOW:
			value = Value.HIGH
		else:
			value = Value.LOW
		
		# set the new value
		gpioObj.setValue(value)
		print('GPIO%d set to: %s' % (gpioNum, value.name))
		
		time.sleep(5)
