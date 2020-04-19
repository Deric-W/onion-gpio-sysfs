import onionGpio
from __future__ import print_function

pin = 14

print('> Instantiating gpio object')
gpio14 = onionGpio.OnionGpio(pin)

print('> Set direction to input... ')
gpio14.setInputDirection()

print('> Get direction: ', gpio14.getDirection())

print('> Read value: ', gpio14.getValue())


input('Ready to test output?')

print('> Set direction to output... ')
gpio14.setOutputDirection()

print('> Get direction: ', gpio14.getDirection())

print('> Read value: ', gpio14.getValue())


print('> Set value to 1... ')
gpio14.setValue(onionGpio.GPIO_VALUE_HIGH)

print('> Read value: ', gpio14.getValue())


print('> Set value to 0... ')
gpio14.setValue(onionGpio.GPIO_VALUE_LOW)

print('> Read value: ', gpio14.getValue())


print()
print('> Done!')
