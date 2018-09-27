'''
In python you can specify the default values of the arguments.

If nothing is passed to these formal parameters then the default value gets evaluated

WARNING: the default values is evaluated only once. for example in the listprint method given below

also you can change the name of the function while calling such as
Eg: if function name is hello() then during calling you can specify as h=hello


'''

# defining the function using default argument values
def helloagain(value:str,hel='abhishek',age=21)->None:
    print(value)
    print(hel)
    print(age)
helloagain('what is your name')
helloagain('what is your name','king of kings')
helloagain('what is your name','satan',100)
h=helloagain
h('oye I have changed the name of the function during calling')

def listprint(hel=[]):
    print(hel)
print([1])
print([1,2])

