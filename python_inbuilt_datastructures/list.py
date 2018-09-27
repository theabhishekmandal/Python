'''
    This program is an example of the inbuilt data structure of python like list
'''

# list can hold heterogenous type of data
arr = [1, 'hello', 2.0, 'abhishek']
print(arr)

# have non-negative and negative indexing
# both prints the last element of the list
print(arr[len(arr) - 1])
print(arr[-1])

# slicing a list
print(arr[2:])
print(arr[2:-1])

#printing the elements of the incremental positions
print(arr[::2])
# printing elements of decremental positions
print(arr[-1::-2])





matrix = [
    [1, 2, 3, 11],
    [4, 5, 6, 12],
    [7, 8, 9, 13]
]

# transposing the matrix
transpose = []
for i in range(len(matrix[0])):
    transpose.append([row[i] for row in matrix])

print(transpose)

print(list(zip(*matrix)))

one = ['name', 'rollno', 'class']
two = ['zemen', 12, 'legend']
for i, v in zip(one, two):
    print('what is your {0}? It is {1}'.format(i,v))