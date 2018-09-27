if __name__ == '__main__':

    '''A generator-function is defined like a normal function, but whenever it needs to generate a value, 
    it does so with the yield keyword rather than return. If the body of a def contains yield,
     the function automatically becomes a generator function.'''



    def reverse(arr):
        for i in arr[::-1]:
            yield i

    arr = [1, 2, 3, 4]
    for i in reverse(arr):
        print(i, end = ' ')

    print()

    '''some generator expressions'''

    def sumOfSquares():
        # sum of squares
        print(sum(i * i for i in range(10)))



    def dotProduct():
        xvec = [10, 20, 30]
        yvec = [7, 5, 3]

        print(sum(x * y for x, y in zip(xvec, yvec)))


    def uniqueWords():
        test = "hello world how are you there hello not word ok how world"
        print(set(i for i in test.split(' ')))

    sumOfSquares()
    dotProduct()
    uniqueWords()