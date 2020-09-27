# gpio-sysfs
Module to control GPIOs using the sysfs interface
[original docs](https://docs.onion.io/omega2-docs/gpio-python-module.html) [sysfs docs](https://www.kernel.org/doc/html/v5.5/driver-api/gpio/legacy.html#sysfs-interface-for-userspace-optional)

## Differences

 - error return codes have been removed, catch Exceptions with try/except instead
 - replaced Constants with Enum members, all methods now accept and return those (or raise a `ValueError`)
 - pointless makefile removed
 - the export of the sysfs interface now takes place when the class is initialised instead of when a method is called
    - the sysfs interface has to be unexported to prevent errors
 - the unexport of the sysfs interface now takes place when the `release` method is called instead of when a method finishes
   - has to be called once and is automatically called when using the class as a context manager (`with OnionGpio(i) as gpio:`)
 - added the `supportsDirection` and `supportsEdge` methods to check if these settings can be changed
 - added the `getEdge`, `setEdge` and `waitForEdge` methods
    - `getEdge` returns the edge setting of the GPIO
    - `setEdge(edge)` is setting the edge setting of the GPIO
    - `waitForEdge(timeout=None)` waits for a edge to occur or the `timeout` to run out if not None (raising a `TimeoutError`)
 - added the `ignore_busy` paramter, which ignores the OSError raised when the interface is already exported (default = False)
 - exposed the `setDirection(direction)` method which is setting the direction setting of the GPIO to `direction`
 - exposed the `setActiveLow(active_low)` method which is setting the active_low setting of the GPIO to `active_low` 
 - removed original `setActiveLow` and `setActiveHigh`
 - removed multiple input checks, use the Enums of this module to interact with the methods
    - `Value` contains supported GPIO values
    - `Direction` contains supported GPIO directions
    - `ActiveLow` contains supported active_low settings
    - `Edge` contains supported GPIO edges
 - removed at least one occasion of Error hiding
 - removed the verbose argument, logging should be done by the application itself

## Compatibility

Module compatible with Python >= 3.5

## Install

Run as root: `python3 setup.py install` or use the .whl file
