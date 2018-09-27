if __name__ == '__main__':
    '''Various String Formatting methods'''

    '''repr method: It is similar to str() method but it also adds 
     quotes and backslashes to the end of the output'''
    hel = 'hello\n'
    hel = repr(hel)
    print(hel) # this will print with double quotation and the backslash n


    '''methods such as rjust(), center() and ljust() are used for adjusting
    the alignment of the text with the given number of width'''
    print('\n')
    for i in range(1, 20):
        print(repr(i * 1).center(4), repr(i * 2).center(4), repr(i * 3).center(4), end=' ')
        print()

    for i in range(1, 20):
        print(str(i * 1).ljust(4), str(i * 2).ljust(4), str(i * 3).ljust(4), end=' ')
        print()

    for i in range(1, 20):
        print(str(i * 1).rjust(4), str(i * 2).rjust(4), str(i * 3).rjust(4), end=' ')
        print()
    print('\n')


    '''Another way of doing the above thing is by using str.format() method'''
    # the integer before ':' represents the position of the argument
    # the integer after ':' ensures that the given field will be a minimum number of characters wide
    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x * 2, x * 3))


    '''str.zfill() method to pad a number with zeros on left side'''
    print()
    # the number inside the zfill method denotes the length of the numeric string after adding zeroes
    # if no. inside zfill method is less than the length of actual string then the string is printed as it is
    print('122'.zfill(2))


    '''str.format() basic format'''
    print()
    print('Toady is {} of {}'.format('1', 'July'))

    # A number in the brackets can be used to refer to the position of the object.
    print('{0} and {1}'.format('spam', 'eggs'))
    print('{1} and {0}'.format('spam', 'eggs'))

    # Keyword arguments can also be used
    print('This {food} is {adjective}'.format(adjective = 'absolutely horrible', food = 'spam'))

    # combining positional and keyword arguments arbitrarily
    print('The story of {0}, {1}, and {other}'.format('Bill', 'Manfred', other = 'Georg'))

    # Apply '!a' for ascii(), '!s' for str(), '!r' for repr()
    print('My hovercraft is full of {!s}.'.format('eels'))
    print('My hovercraft is full of {!r}.'.format('eels'))
    print('My hovercraft is full of {!a}.'.format('eels'))

