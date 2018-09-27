# creating set using curly brackets
# set contains only unique elements and not repeated characters
arr ={1, 2, 3, 4, 4, 5, 5, 6}
print(arr)

# set comprehension just like lists
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)