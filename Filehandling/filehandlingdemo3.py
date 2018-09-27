with open('hello2.txt', 'r+') as f:
    hello = f.read()    # reading all the contents of the file
    print(hello)
    print()
    f.seek(0)           # reinitialising the file ptr to beginning
    hello = f.readline()# reading a single line from the file
    print(hello)
    print()
    f.seek(0)           # reinitialising the file ptr to beginning
    hello = f.readlines()# reading all the contents of the file and returning in the form of list
    print(hello)
