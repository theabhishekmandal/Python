if __name__ == '__main__':
    '''This is an example of raise.
      1. Raise helps in raising your own errors
      2. To reraise the current exception in an exception handler, so that it can be handled further up
        the call stack 
    
    '''

    '''if you want to raise an exception and want to handle it then use this'''
    try:
        print('Raising exception')
        raise ZeroDivisionError
    except ZeroDivisionError:
        print('division by zero is being performed')
