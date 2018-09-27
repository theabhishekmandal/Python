def min():
    pass

'''here we are showing what happens if a variable is found in the global scope which is already present in the 
    built-in'''

'''
    This code will give error because min is a built in which finds the minimum value from an iterator.
    But the min function is found in the global scope before than the built-in of the LEGB order. So that's why it is 
    giving error
'''
m = min([1, 2, 3, 4])
print(m)