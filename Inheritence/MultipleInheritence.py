'''
    Multiple inheritance causes diamond problem i.e. If a subclass is derived from a number of base classes
    and each of the base classes have the same method. So when the base class tries to call the same name method
    then which method gets invoked.

    In python this problem is resolved by the order in which the base classes are extended. In the example below
    baseclass2 is extended first. If the samename method is found in this then it gets invoked otherwise, python
    searches for the samename method in next baseclass
'''
class Baseclass1:

    def call(self):
        print('hello from base class 1')


class Baseclass2:

    def call(self):
        print('hello from base class 2')


class Baseclass3:

    def call(self):
        print('hello from base class 3')


class subclass(Baseclass2, Baseclass1, Baseclass3):

    def call(self):
        super(subclass, self).call()



ob = subclass()
ob.call()