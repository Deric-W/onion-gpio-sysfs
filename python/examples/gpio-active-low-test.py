import onionGpio
from __future__ import print_function

pin = 14

print('> Instantiating gpio object')
gpio14 	= onionGpio.OnionGpio(pin)

print('> Set active-high')
gpio14.setActiveLowFalse()

print('> Get active-low: ', gpio14.getActiveLow())

print('> Set direction to input...')
gpio14.setInputDirection()

print('> Get direction: ', gpio14.getDirection())

print('> Read value: ', gpio14.getValue())


input('Ready to test output?')

print('> Set direction to output...')
gpio14.setOutputDirection()

print('> Get direction: ', gpio14.getDirection())

print('> Read value: ', gpio14.getValue())


print('> Set value to 1...')
gpio14.setValue(onionGpio.GPIO_VALUE_HIGH)

print('> Read value: ', gpio14.getValue())


print('> Set value to 0...')
gpio14.setValue(onionGpio.GPIO_VALUE_LOW)

print('> Read value: ', gpio14.getValue())


input('Ready to test active low?')

print('> Set direction to input...')
gpio14.setInputDirection()

print('> Get direction: ', gpio14.getDirection())

print('> Get active-low: ', gpio14.getActiveLow())

print('> Read value: ', gpio14.getValue())


print('> Set to active-low...')
gpio14.setActiveLowTrue()

print('> Get active-low: ', gpio14.getActiveLow())

print('> Read value: ', gpio14.getValue())


print()
print('> Done!')
