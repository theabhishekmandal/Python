x = 'global x'


''' if you want to use the global variable inside a method then use the keyword global inside the function'''

def test():
    global x
    x = 'local x'
    print(x)

test()
print(x)
