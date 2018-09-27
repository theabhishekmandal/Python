if __name__ == '__main__':
    print('''using try and except for using exception''')
    try:
        # here if you press any character other than numerals then it throws exception
        number = int(input('enter a alphabet or a string\n').strip())
        print(number)
    except ValueError:
        print('Not a number')


