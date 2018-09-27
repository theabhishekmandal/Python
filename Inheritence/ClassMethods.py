'''
    This is the implementation of the isinstance and issubclass method

'''
class A:
    pass
class B(A):
    pass

ob1 = A()
ob2 = B()

print(isinstance(ob1, B))
print(isinstance(ob1, A))

print(isinstance(ob2, A))
print(isinstance(ob2, B))

print(issubclass(B, A))
print(issubclass(A, B))