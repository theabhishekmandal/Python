if __name__ == '__main__':
    '''An exception can have many exception clause'''
    try:
        arr = ['hello', 'world', 'i', 'am']
        # if input is given non numerical character then it will throw ValueError exception
        index = int(input().strip())

        # if index is given which is not present then indexerror exception will be thrown
        print(arr[index])

        # if 0 is provided then zeroDivisionError exception will be thrown
        print(1 / index)
    except (ZeroDivisionError, IndexError, ValueError) as error:
        print('You did ' + str(error))
