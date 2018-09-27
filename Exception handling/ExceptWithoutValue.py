import sys

if __name__ == '__main__':
    '''This is an example of exception in which we can omit the name of the exception.
       This type of exception is used at extreme condition. Because the actual error is
       not visible i.e what type of error generated this type of exception'''
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise