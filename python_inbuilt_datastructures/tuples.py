arr = 1, 'abhishek', 'mandal'  # initialising a tuple
print(arr)

# nested tuple
arr = 'hello', ("it's me", 'I ', 'was ', 'wondering'),  1234
print(arr)

#tuples arre immutable i.e their value cannot change
# arr[0] = 'hello' shows error

#tuples can contain mutable object
arr = [1,2,4], ['i', 'love', 'pav bhaji'], 'very', 'much'
print(arr)
arr[1][2] = 'gol gappe'
print(arr)
print()


# assigning tuple values to variables
a,b,c,d = arr
print(a)
print(b)
print(c)
print(d)


# creating a single tuple and 0 len tuple
empty = ()
print(type(empty))

singleton = 'this is single tuple see the comma',
print(singleton, type(singleton))