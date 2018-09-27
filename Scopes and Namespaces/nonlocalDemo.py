''' Here in this nonlocal keyword usage is implemented.
    nonlocal is used when inner function has the same variable as that of the enclosing function.
    But you want to use the enclosing function variable.
'''

def outer():
    x = 'outer x'

    def inner():
        # as x is declared as nonlocal, then the enclosing function x variable is used.
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()