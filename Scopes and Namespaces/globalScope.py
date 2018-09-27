x = 'global x'
def test() -> None:
    y = 'local y'
    print(x)

'''There are four types of scopes in python denoted by LEGB
    L - Local
    E - Enclosing
    G - Global
    B - Built-in
    Python checks for something in the LEGB order
'''

'''on calling the function first python searches in LEGB order. x variable is found in global scope
    and the value it's value is used'''

test()
print(x)