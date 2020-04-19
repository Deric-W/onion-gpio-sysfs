## EXAMPLE CODE
# Set the GPIO to output, read and print the initial value

import onionGpio
from __future__ import print_function

gpioNum = 6
gpioObj	= onionGpio.OnionGpio(gpioNum)

# set to input 
gpioObj.setOutputDirection()
print('GPIO%d set to output,' % gpioNum, end="")

# read the value
value = gpioObj.getValue()
print(' initial value: %d' % value)

## GOING FURTHER
# Try changing line 10 to: 
#  gpioObj.setOutputDirection(onionGpio.GPIO_OUTPUT_DIRECTION_LOW)
# or
#  gpioObj.setOutputDirection(onionGpio.GPIO_OUTPUT_DIRECTION_HIGH)
#
# And see how the initial value changes :)
#
