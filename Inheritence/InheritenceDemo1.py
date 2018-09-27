'''This example shows that there are two ways to access the method of the superclass
    Go to function getlength()
'''
class Square:
    def __init__(self, side):
        self.__side = side

    def getside(self):
        return self.__side

    def area(self):
        return self.__side ** 2


class Rectangle(Square):
    def __init__(self, length, width):
        super(Rectangle, self).__init__(length)
        self.__width = width

    def getlength(self):

        # one way to get the super class member function
        return Square.getside(self)

        # second way to get the super class member functions
        # return super(Rectangle, self).getside()

    def area(self):
        return self.getlength() * self.__width


rectangle = Rectangle(10, 20)
print(rectangle.area())