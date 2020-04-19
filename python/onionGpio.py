#!/usr/bin/python3

"Module for interfacing with gpio pins on the onion"

import errno
from select import select

__version__ = '0.2'
__author__ = 'Lazar, Justin Duplessis and Eric Wolf'
__maintainer__ = 'Eric Wolf'    # for this fork
__email__ = "robo-eric@gmx.de"
__contact__ = "https://github.com/Deric-W/onion-gpio-sysfs"


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

class OnionGpio:    # sysfs documentation: https://www.kernel.org/doc/Documentation/gpio/sysfs.txt

    """Base class for sysfs GPIO access"""

    def __init__(self, gpio, ignore_busy=False):
        """init with the gpio pin number and if the interface being used should be ignored"""
        self.gpio = gpio    # gpio number
        path = GPIO_PATH % self.gpio   # directory containing the gpio files
        self.gpioValueFile = path + '/' + GPIO_VALUE_FILE  # file to set/get value
        self.gpioDirectionFile = path + '/' + GPIO_DIRECTION_FILE  # file to set/get direction
        self.gpioActiveLowFile = path + '/' + GPIO_ACTIVE_LOW_FILE # file to set/get active_low
        self.gpioEdgeFile = path + '/' + GPIO_EDGE_FILE # file to set/get edge
        try:
            initGpio(gpio)  # init gpio sysfs interface
        except OSError as err:
            if err.errno == errno.EBUSY and ignore_busy:    # interface already in use but we should ignore
                pass
            else:   # something else happend or we should not ignore the busy interface
                raise

    def release(self):
        """release gpio sysfs interface"""  # call once per object
        freeGpio(self.gpio)

    # context manager methods

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.release()  # dont call inside context manager
        return False    # we dont want to hide exceptions

    # value functions

    def getValue(self):
        """Read current GPIO value"""
        with open(self.gpioValueFile, 'r') as fd:
            return int(fd.read())   # catch ValueError if file content not integer


    def setValue(self, value):
        """Set the desired GPIO value"""
        with open(self.gpioValueFile, 'w') as fd:
            fd.write(str(value))


    def setValueLow(self):
        """set gpio value to low"""
        self.setValue(GPIO_VALUE_LOW)


    def setValueHigh(self):
        """set gpio value to high"""
        self.setValue(GPIO_VALUE_HIGH)

    # direction functions

    def getDirection(self):
        """Read current GPIO direction"""
        # read from the direction file
        with open(self.gpioDirectionFile, 'r') as fd:
            return fd.read().rstrip("\n")


    def setDirection(self, direction):
        """Set the desired GPIO direction"""
        # write to the direction file
        with open(self.gpioDirectionFile, 'w') as fd:
            fd.write(direction)


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
        with open(self.gpioActiveLowFile, 'r') as fd:
            return int(fd.read())   # catch ValueError if file content not integer


    def setActiveLow(self, activeLow):
        """Set the desired GPIO direction"""
        with open(self.gpioActiveLowFile, 'w') as fd:
            fd.write(str(activeLow))
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
        with open(self.gpioEdgeFile, "r") as fd:
            return fd.read().rstrip("\n")


    def setEdge(self, edge):
        """set edge setting of gpio"""
        with open(self.gpioEdgeFile, "w") as fd:
            fd.write(edge)
        # note: edge setting is reset when the gpio sysfs interface
        # is released!


    def waitForEdge(self, edge=None, timeout=None):
        """wait for edge on gpio"""
        if edge is not None:
            self.setEdge(edge)
        with open(self.gpioValueFile, "r") as fd:
            fd.read()   # somehow needs to be read before using select to work
            select([], [], [fd], timeout)    # wait for value file exceptional condition


def initGpio(gpio):
    """Write to the gpio export to make the gpio available in sysfs"""
    with open(GPIO_EXPORT, 'w') as fd:
        fd.write(str(gpio))

def freeGpio(gpio):
    """Write to the gpio unexport to release the gpio sysfs interface"""
    with open(GPIO_UNEXPORT, 'w') as fd:
        fd.write(str(gpio))
