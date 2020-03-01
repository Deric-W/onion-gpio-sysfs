## EXAMPLE CODE
# Set a GPIO to output, and alternate the output between LOW and HIGH every 5 seconds

import time
import onionGpio

gpioNum = 1
gpioObj	= onionGpio.OnionGpio(gpioNum)

# set to output 
gpioObj.setOutputDirection(onionGpio.GPIO_VALUE_LOW)		# initialize the GPIO to 0 (LOW)

# alternate the value
value = onionGpio.GPIO_VALUE_LOW
while True:
	# reverse the value
	if value == onionGpio.GPIO_VALUE_LOW:
		value = onionGpio.GPIO_VALUE_HIGH
	else:
		value = onionGpio.GPIO_VALUE_LOW
	
	# set the new value
	gpioObj.setValue(value)
	print('GPIO%d set to: %d' % (gpioNum, value))
	
	time.sleep(5)
