'''
In this function example we are implementing that ,there can be arbitrary number of arguments
'''
def hello(*args,sep=' '):
    return sep.join(args)
print(hello('abhishek','mandal','is','here'))
print(hello('what','are','you'))