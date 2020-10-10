#!/usr/bin/python3

"Module for interfacing with gpio pins using the linux sysfs interface"

__version__ = "0.3"
__author__ = 'Lazar, Justin Duplessis and Eric Wolf'
__maintainer__ = "Eric Wolf"    # for this fork
__email__ = "robo-eric@gmx.de"
__contact__ = "https://github.com/Deric-W/onion-gpio-sysfs"

from os.path import isfile
from errno import EBUSY
from enum import Enum
from typing import Optional
from select import select

# file paths
GPIO_BASE_PATH = "/sys/class/gpio"
GPIO_EXPORT_PATH = GPIO_BASE_PATH + "/export"
GPIO_UNEXPORT_PATH = GPIO_BASE_PATH + "/unexport"
GPIO_PATH = GPIO_BASE_PATH + "/gpio%d"

# file names
GPIO_VALUE_FILE = "value"
GPIO_DIRECTION_FILE = "direction"
GPIO_ACTIVE_LOW_FILE = "active_low"
GPIO_EDGE_FILE = "edge"


class Value(Enum):
    """Enum representing the logical state"""
    LOW = "0"
    HIGH = "1"


class Direction(Enum):
    """Enum representing the direction"""
    INPUT = "in"
    OUTPUT = "out"
    OUTPUT_LOW = "low"
    OUTPUT_HIGH = "high"


class ActiveLow(Enum):
    """Enum representing the active_low status"""
    HIGH = "0"
    LOW = "1"


class Edge(Enum):
    """Enum representing the edge status"""
    NONE = "none"
    RISING = "rising"
    FALLING = "falling"
    BOTH = "both"


class OnionGpio:    # sysfs documentation: https://www.kernel.org/doc/Documentation/gpio/sysfs.txt

    """Base class for sysfs GPIO access"""

    def __init__(self, gpio: int, ignore_busy: bool = False) -> None:
        """init with the gpio pin number and if the interface being used should be ignored"""
        self.gpio = gpio    # gpio number
        path = GPIO_PATH % self.gpio   # directory containing the gpio files
        self.gpioValueFile = path + '/' + GPIO_VALUE_FILE  # file to set/get value
        self.gpioDirectionFile = path + '/' + GPIO_DIRECTION_FILE  # file to set/get direction
        self.gpioActiveLowFile = path + '/' + GPIO_ACTIVE_LOW_FILE  # file to set/get active_low
        self.gpioEdgeFile = path + '/' + GPIO_EDGE_FILE  # file to set/get edge
        try:
            initGpio(gpio)  # init gpio sysfs interface
        except OSError as err:
            if err.errno == EBUSY and ignore_busy:    # interface already in use but we should ignore
                pass
            else:   # something else happend or we should not ignore the busy interface
                raise

    def release(self) -> None:
        """release gpio sysfs interface"""  # call once per object
        freeGpio(self.gpio)

    # context manager methods

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.release()  # dont call inside context manager
        return False    # we dont want to hide exceptions

    # value functions

    def getValue(self) -> Value:
        """Read current GPIO value"""
        with open(self.gpioValueFile, 'r') as fd:
            return Value(fd.readline().rstrip("\n"))   # catch ValueError if file content is not 0 or 1

    def setValue(self, value: Value) -> None:
        """Set the desired GPIO value"""
        with open(self.gpioValueFile, 'w') as fd:
            fd.write(value.value)

    # direction functions

    def supportsDirection(self) -> bool:
        """check if the gpio supports setting the direction"""
        return isfile(self.gpioDirectionFile)

    def getDirection(self) -> Direction:
        """Read current GPIO direction"""
        # read from the direction file
        with open(self.gpioDirectionFile, 'r') as fd:
            return Direction(fd.readline().rstrip("\n"))    # catch ValueError if file content not valid

    def setDirection(self, direction: Direction) -> None:
        """Set the desired GPIO direction"""
        # write to the direction file
        with open(self.gpioDirectionFile, 'w') as fd:
            fd.write(direction.value)

    # active-low functions

    def getActiveLow(self) -> ActiveLow:
        """Read if current GPIO is active-low"""
        with open(self.gpioActiveLowFile, 'r') as fd:
            return ActiveLow(fd.readline().rstrip("\n"))   # catch ValueError if file content not valid

    def setActiveLow(self, active_low: ActiveLow) -> None:
        """Set the desired GPIO direction"""
        with open(self.gpioActiveLowFile, 'w') as fd:
            fd.write(active_low.value)
        # note: active_low setting is reset when the gpio sysfs interface
        # is released!

    # edge methods

    def supportsEdge(self) -> bool:
        """check if the gpio supports edges"""
        return isfile(self.gpioEdgeFile)

    def getEdge(self) -> Edge:
        """get edge setting of gpio"""
        with open(self.gpioEdgeFile, "r") as fd:
            return Edge(fd.readline().rstrip("\n"))     # catch ValueError if file content not valid

    def setEdge(self, edge: Edge) -> None:
        """set edge setting of gpio"""
        with open(self.gpioEdgeFile, "w") as fd:
            fd.write(edge.value)
        # note: edge setting is reset when the gpio sysfs interface
        # is released!

    def waitForEdge(self, timeout: Optional[float] = None) -> None:
        """wait for edge on gpio"""
        with open(self.gpioValueFile, "r") as fd:
            fd.read()   # somehow needs to be read before using select to work
            if fd not in select([], [], [fd], timeout)[2]:    # wait for value file exceptional condition
                raise TimeoutError("received no edge on gpio {0}".format(self.gpio))


def initGpio(gpio: int) -> None:
    """Write to the gpio export to make the gpio available in sysfs"""
    with open(GPIO_EXPORT_PATH, 'w') as fd:
        fd.write(str(gpio))


def freeGpio(gpio: int) -> None:
    """Write to the gpio unexport to release the gpio sysfs interface"""
    with open(GPIO_UNEXPORT_PATH, 'w') as fd:
        fd.write(str(gpio))
