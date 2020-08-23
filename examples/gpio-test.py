from onionGpio import OnionGpio, Direction, Value


print('> Instantiating gpio object')
with OnionGpio(14) as gpio14:

    print('> Set direction to input... ')
    gpio14.setDirection(Direction.INPUT)

    print('> Get direction: ', gpio14.getDirection())

    print('> Read value: ', gpio14.getValue())


    input('Ready to test output?')

    print('> Set direction to output... ')
    gpio14.setDirection(Direction.OUTPUT)

    print('> Get direction: ', gpio14.getDirection())

    print('> Read value: ', gpio14.getValue())


    print('> Set value to 1... ')
    gpio14.setValue(Value.HIGH)

    print('> Read value: ', gpio14.getValue())


    print('> Set value to 0... ')
    gpio14.setValue(Value.LOW)

    print('> Read value: ', gpio14.getValue())


print()
print('> Done!')
