'''This is an example of enclosing scope'''
def outer():
    x = 'outer x'
    def inner():
        # x = 'inner x'
        ''' This x is searched first inside the local scope. Then it is searched in the local scope of the
            enclosing function. It is found so it's value is printed.
        '''
        print(x)
    inner()
    print(x)
outer()