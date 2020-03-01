# gpio-sysfs
Module to control GPIOs using the sysfs interface
[original docs](https://docs.onion.io/omega2-docs/gpio-python-module.html)

## Differences

 - return codes have been removed, catch Exceptions with try/except instead
 - `getValue` does now return a interger (or raises a `ValueError`)
 - pointless makefile removed
 - the unexport of the sysfs interface now takes place even if a Exception occured to prevent blocking the interface
 - added the `setValueLow` and `setValueHigh` convenience methods
 - exposed the `setDirection` method
 - exposed the `setActiveLow` method
 - renamed original `setActiveLow` and `setActiveHigh` to `setActiveLowLow` and `setActiveLowHigh`
 - removed multiple input checks, use the constants of this module to interact with the methods or use the convenience methods
 - removed at least one occasion of Error hiding
 - removed the verbose argument, logging should be done by the application itself

## Compatibility

Module now comptatible with all versions of Python !

## Install

Run as root: `cp python/onionGpio.py /usr/lib/<PYTHON_VERSION>/onionGpio.py`
