"module for interfacing with gpio pins on the onion"
from select import select

__version__ = '0.2'
__author__ = 'Lazar, Justin Duplessis and Eric Wolf'
__maintainer__ = 'Eric Wolf'    # for this fork


# file paths
GPIO_BASE_PATH = '/sys/class/gpio'
GPIO_EXPORT = GPIO_BASE_PATH + '/export'
GPIO_UNEXPORT = GPIO_BASE_PATH + '/unexport'

GPIO_PATH = GPIO_BASE_PATH + '/gpio%d'
GPIO_VALUE_FILE = 'value'
GPIO_DIRECTION_FILE = 'direction'
GPIO_ACTIVE_LOW_FILE = 'active_low'
GPIO_EDGE_FILE = 'edge'

# gpio values
GPIO_VALUE_LOW = 0
GPIO_VALUE_HIGH = 1

# gpio directions
GPIO_INPUT_DIRECTION = 'in'
GPIO_OUTPUT_DIRECTION = 'out'
GPIO_OUTPUT_DIRECTION_LOW = 'low'
GPIO_OUTPUT_DIRECTION_HIGH = 'high'

# gpio active_low options
GPIO_ACTIVE_HIGH = 0
GPIO_ACTIVE_LOW = 1

# gpio edges
GPIO_EDGE_NONE = 'none'
GPIO_EDGE_RISING = 'rising'
GPIO_EDGE_FALLING = 'falling'
GPIO_EDGE_BOTH = 'both'

class OnionGpio:

    """Base class for sysfs GPIO access"""

    def __init__(self, gpio):
        self.gpio = gpio    # gpio number
        path = GPIO_PATH % self.gpio   # directory containing the gpio files
        self.gpioValueFile = path + '/' + GPIO_VALUE_FILE  # file to set/get value
        self.gpioDirectionFile = path + '/' + GPIO_DIRECTION_FILE  # file to set/get direction
        self.gpioActiveLowFile = path + '/' + GPIO_ACTIVE_LOW_FILE # file to set/get active_low
        self.gpioEdgeFile = path + '/' + GPIO_EDGE_FILE # file to set/get edge


    def _initGpio(self):
        """Write to the gpio export to make the gpio available in sysfs"""

        with open(GPIO_EXPORT, 'w') as fd:
            fd.write(str(self.gpio))


    def _freeGpio(self):
        """Write to the gpio unexport to release the gpio sysfs instance"""

        with open(GPIO_UNEXPORT, 'w') as fd:
            fd.write(str(self.gpio))

    # value functions

    def getValue(self):
        """Read current GPIO value"""

        # generate the gpio sysfs instance
        self._initGpio()

        try:
            with open(self.gpioValueFile, 'r') as fd:
                return int(fd.read())   # catch ValueError if file content not integer
        finally:    # release the gpio sysfs instance
            self._freeGpio()


    def setValue(self, value):
        """Set the desired GPIO value"""

        # generate the gpio sysfs instance
        self._initGpio()

        try:
            with open(self.gpioValueFile, 'w') as fd:
                fd.write(str(value))
        finally:    # release the gpio sysfs instance
            self._freeGpio()


    def setValueLow(self):
        """set gpio value to low"""
        self.setValue(GPIO_VALUE_LOW)


    def setValueHigh(self):
        """set gpio value to high"""
        self.setValue(GPIO_VALUE_HIGH)

    # direction functions

    def getDirection(self):
        """Read current GPIO direction"""

        # generate the gpio sysfs instance
        self._initGpio()

        try:
            # read from the direction file
            with open(self.gpioDirectionFile, 'r') as fd:
                return fd.read().rstrip("\n")

        finally:    # release the gpio sysfs instance
            self._freeGpio()


    def setDirection(self, direction):
        """Set the desired GPIO direction"""

        # generate the gpio sysfs instance
        self._initGpio()

        try:
            # write to the direction file
            with open(self.gpioDirectionFile, 'w') as fd:
                fd.write(direction)
        finally:    # release the gpio sysfs instance
            self._freeGpio()


    def setInputDirection(self):
        """Set direction to input"""
        self.setDirection(GPIO_INPUT_DIRECTION)


    def setOutputDirection(self, initial=None):
        """Set the direction to output and set initial value"""
        if initial is None:
            self.setDirection(GPIO_OUTPUT_DIRECTION)
        elif initial == GPIO_VALUE_LOW:
            self.setDirection(GPIO_OUTPUT_DIRECTION_LOW)
        elif initial == GPIO_VALUE_HIGH:
            self.setDirection(GPIO_OUTPUT_DIRECTION_HIGH)
        else:
            raise ValueError("initial not supported")

    # active-low functions

    def getActiveLow(self):
        """Read if current GPIO is active-low"""

        # generate the gpio sysfs instance
        self._initGpio()

        try:
            with open(self.gpioActiveLowFile, 'r') as fd:
                return int(fd.read())   # catch ValueError if file content not integer
        finally:    # release the gpio sysfs instance
            self._freeGpio()


    def setActiveLow(self, activeLow):
        """Set the desired GPIO direction"""

        # generate the gpio sysfs instance
        self._initGpio()

        try:
            with open(self.gpioActiveLowFile, 'w') as fd:
                fd.write(str(activeLow))
        finally:    # release the gpio sysfs instance
            self._freeGpio()
        # note: active_low setting is reset when the gpio sysfs interface
        # is released!


    def setActiveLowFalse(self):
        """set active_low to not invert"""
        self.setActiveLow(GPIO_ACTIVE_HIGH)


    def setActiveLowTrue(self):
        """set active_low to invert"""
        self.setActiveLow(GPIO_ACTIVE_LOW)

    # edge methods

    def getEdge(self):
        """get edge setting of gpio"""
        self._initGpio()
        try:
            with open(self.gpioEdgeFile, "r") as fd:
                return fd.read().rstrip("\n")
        finally:
            self._freeGpio()

    # setEdge would be pointless because it is reset when the sysfs interface is released,
    # use waitForEdge instead

    def waitForEdge(self, edge, timeout=None):
        """wait for edge on gpio"""
        self._initGpio()
        try:
            with open(self.gpioEdgeFile, "w") as fd:
                fd.write(edge)
            with open(self.gpioValueFile, "r") as fd:
                fd.read()   # somehow needs to be read befor using select to work
                select([], [], [fd], timeout)    # wait for value file exceptional condition
        finally:
            self._freeGpio()
