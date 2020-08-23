from onionGpio import OnionGpio, ActiveLow, Direction, Value


print('> Instantiating gpio object')
with OnionGpio(14) as gpio14:

    print('> Set active-high')
    gpio14.setActiveLow(ActiveLow.HIGH)

    print('> Get active-low: ', gpio14.getActiveLow())

    print('> Set direction to input...')
    gpio14.setDirection(Direction.INPUT)

    print('> Get direction: ', gpio14.getDirection())

    print('> Read value: ', gpio14.getValue())


    input('Ready to test output?')

    print('> Set direction to output...')
    gpio14.setDirection(Direction.OUTPUT)

    print('> Get direction: ', gpio14.getDirection())

    print('> Read value: ', gpio14.getValue())


    print('> Set value to 1...')
    gpio14.setValue(Value.HIGH)

    print('> Read value: ', gpio14.getValue())


    print('> Set value to 0...')
    gpio14.setValue(Value.LOW)

    print('> Read value: ', gpio14.getValue())


    input('Ready to test active low?')

    print('> Set direction to input...')
    gpio14.setDirection(Direction.INPUT)

    print('> Get direction: ', gpio14.getDirection())

    print('> Get active-low: ', gpio14.getActiveLow())

    print('> Read value: ', gpio14.getValue())


    print('> Set to active-low...')
    gpio14.setActiveLow(ActiveLow.LOW)

    print('> Get active-low: ', gpio14.getActiveLow())

    print('> Read value: ', gpio14.getValue())


print()
print('> Done!')
