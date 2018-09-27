class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
if __name__ == '__main__':
    '''An exception subclass must come before its superclass.
    This is because except clause that uses a superclass will catch exceptions of its type 
    and all of it's subclasses'''

    # here the except clause is in increasing order i.e
    # from subclass to super class
    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print('D')
        except C:
            print("C")
        except B:
            print("B")

    print()

    # if we write the exception clause from superclass to subclasses
    # then all the answer will be B B B
    for cls in [B, C, D]:
        try:
            raise cls()
        except B:
            print('B')
        except C:
            print('C')
        except D:
            print('D')
