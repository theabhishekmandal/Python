'''
This program is an example of unpacking the elements of the list
'''
def foo(name, age, profession):
    print(name)
    print(age)
    print(profession)

about = ['abhishek mandal', 20, 'student']
foo(*about)       # this is called unpacking of the argument list 