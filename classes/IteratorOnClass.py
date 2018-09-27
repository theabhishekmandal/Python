'''Implementing iterator to print the string'''
class String:
    def __init__(self, data, index = 0):
        self.data = data
        self.index = index

    def __iter__(self):
        return self

    def __next__(self):
        if self.index is len(self.data):
            raise StopIteration
        val = self.data[self.index]
        self.index += 1
        return val

'''Implementing iterator to print string in reverse order'''
class String2(String):
    def __init__(self, data):
        super(String2, self).__init__(data, len(data))

    def __iter__(self):
        return self

    def __next__(self):
        if self.index is 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

val = String('abhishek')
for i in val:
    print(i, end = ' ')

print()

val =  String2('abhishek')
for i in val:
    print(i, end = ' ')