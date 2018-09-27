class test:
    i = 1234

    def f(self):
        print('hello world')

'''These are called attribute references i.e accessing the class members using the class name
    Here it returns an integer and a function object. Note that it does not call the function
'''
print(test.f)
print(test.i)

'''
    now below example is called instantiation. Through the object created we can use the class members and 
    can call the member functions
'''

ob = test()

print(ob.i)
print(ob.f())