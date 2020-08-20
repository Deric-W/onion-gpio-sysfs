## EXAMPLE CODE
# Set the GPIO to output, read and print the initial value

from onionGpio import OnionGpio, Direction


gpioNum = 6
with OnionGpio(gpioNum) as gpioObj: 
    gpioObj.setDirection(Direction.OUTPUT)
    print('GPIO%d set to output,' % gpioNum, end="")

    # read the value
    print(' initial value: %s' % gpioObj.getValue().name)

    ## GOING FURTHER
    # Try changing line 10 to: 
    #  gpioObj.setDirection(Direction.OUTPUT_LOW)
    # or
    #  gpioObj.setDirection(Direction.OUTPUT_HIGH)
    #
    # And see how the initial value changes :)
    #
