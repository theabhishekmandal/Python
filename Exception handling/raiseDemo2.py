if __name__ == '__main__':
    '''re raising exception example based on previous example'''
    '''if you want to raise an exception and don't want to handle it then use this'''
    try:
        print("Raising exceptions")
        raise ZeroDivisionError
    except Exception:
        print('some exception flew by')
        raise             # here raise will send the exception to the default exception handler