if __name__ == '__main__':
    '''There are some clean up actions that are needed to be performed even when everything excutes correctly or not.
        These are some types of lines which are needed to be closed under all circumstances'''
    try:
        raise Exception
    except Exception as err:
        print('I am the error')
    finally:
        print('I will be there if everything is finished')