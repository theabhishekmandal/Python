x = 'global x'

# this method found the value of x in it's local scope so it printed the current value
def test() -> None:
    x = 'local x'
    print(x)

test()
print(x)