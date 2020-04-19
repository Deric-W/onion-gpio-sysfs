# gpio-sysfs
Module to control GPIOs using the sysfs interface
[original docs](https://docs.onion.io/omega2-docs/gpio-python-module.html) [sysfs docs](https://www.kernel.org/doc/html/v5.5/driver-api/gpio/legacy.html#sysfs-interface-for-userspace-optional)

## Differences

 - error return codes have been removed, catch Exceptions with try/except instead
 - `getValue` and `getActiveLow` do now return a interger (or raise a `ValueError`)
 - pointless makefile removed
 - the export of the sysfs interface now takes place when the class is initialised instead of when a method is called
    - the sysfs interface has to be unexported to prevent errors
 - the unexport of the sysfs interface now takes place when the `release` method is called instead of when a method finishes
   - has to be called once and is automatically called when using the class as a context manager (`with OnionGpio(i) as gpio:`)
 - added the `setValueLow` and `setValueHigh` convenience methods
 - added the `getEdge`, `setEdge` and `waitForEdge` methods
    - `getEdge` returns the edge setting of the GPIO as string
    - `setEdge(edge)` is setting the edge setting of the GPIO
    - `waitForEdge(edge=None, timeout=None)` is setting the `edge` if not `None` and waits for it to occur or the `timeout` to run out if not None
 - added the `ignore_busy` paramter, which ignores the OSError raised when the interface is already exported (default = False)
 - exposed the `setDirection(direction)` method which is setting the direction setting of the GPIO to `direction`
 - exposed the `setActiveLow(active_low)` method which is setting the active_low setting of the GPIO to `active_low` 
 - renamed original `setActiveLow` and `setActiveHigh` to `setActiveLowTrue` and `setActiveLowFalse`
 - removed multiple input checks, use the constants of this module to interact with the methods or use the convenience methods
    - `GPIO_VALUE_*` contains supported GPIO values
    - `GPIO_DIRECTION_*` contains supported GPIO directions
    - `GPIO_ACTIVE_*` contains supported active_low settings
    - `GPIO_EDGE_*` contains supported GPIO edges
 - removed at least one occasion of Error hiding
    - `setOutputDirection` now raises `ValueError` if the initial is not supported
 - removed the verbose argument, logging should be done by the application itself

## Compatibility

Module now compatible with all versions of Python !

Examples now compatible with Python 3

## Install

Run as root: `cp python/onionGpio.py /usr/lib/<PYTHON_VERSION>/onionGpio.py`
