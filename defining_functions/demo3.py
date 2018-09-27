'''This function example tells that you can pass keyword arguments.
they are of the type kwarg=keyword.

Also their is a notation of keyword arguemnts and default arguments:
       def function-name(*args,**kwargs)
the *args is passed as a tuple containing positional values
the **kwargs is passed as a dictionary

the order in which they are passed are printed or evaluated in the same order

'''

# keyword argument example
def showmesomething(name,city='New Delhi',State='Delhi'):
    print('Name',name,)
    print('City',city,)
    print('State',State)
    print()

s=showmesomething
s('abhishek')
s(name='abhishrey',State='Uttar Pradesh',city='Tundla')
s(name='ashu',city='Sitapur',State='Uttar pradesh')


# *args and **kwargs example
def show(*args,**kwargs):
    print(type(args))
    for i in args:
        print(i)

    print()
    print(type(kwargs))
    for k in kwargs:
        print(k+': '+kwargs[k])
    print()

show('hello','this','is','passed','as','tuple',type='dicitonary',values='passed')
show("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
