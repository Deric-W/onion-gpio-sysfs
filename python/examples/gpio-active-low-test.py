import onionGpio

pin = 14

print '> Instantiating gpio object'
gpio14 	= onionGpio.OnionGpio(pin)
print ''

print '> Set active-high: '
ret 	= gpio14.setActiveHigh()
print '    returned %d'%ret

print '> Get active-low: ',
activeLow 	= gpio14.getActiveLow()
print activeLow

print '> Set direction to input... '
ret 	= gpio14.setInputDirection()
print '    returned %d'%ret

print '> Get direction: ',
direction 	= gpio14.getDirection()
print direction

print '> Read value: ',
val		= gpio14.getValue()
print val



raw_input('Ready to test output?')

print '> Set direction to output... '
ret 	= gpio14.setOutputDirection()
print '    returned %d'%ret

print '> Get direction: ',
direction 	= gpio14.getDirection()
print direction


print '> Read value: ',
val		= gpio14.getValue()
print val


print '> Set value to 1... '
ret		= gpio14.setValue(1)
print '    returned %d'%ret

print '> Read value: ',
val		= gpio14.getValue()
print val


print ''
print '> Set value to 0... '
ret		= gpio14.setValue(1)
print '    returned %d'%ret

print '> Read value: ',
val		= gpio14.getValue()
print val




raw_input('Ready to test active low?')

print '> Set direction to input... '
ret 	= gpio14.setInputDirection()
print '    returned %d'%ret

print '> Get direction: ',
direction 	= gpio14.getDirection()
print direction


print '> Get active-low: ',
activeLow 	= gpio14.getActiveLow()
print activeLow


print '> Read value: ',
val		= gpio14.getValue()
print val

print '> Set to active-low... '
ret		= gpio14.setActiveLow()
print '    returned %d'%ret


print '> Get active-low: ',
activeLow 	= gpio14.getActiveLow()
print activeLow

print '> Read value: ',
val		= gpio14.getValue()
print val




print ''
print '> Done!'
