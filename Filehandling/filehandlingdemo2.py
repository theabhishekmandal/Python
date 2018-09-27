if __name__ == '__main__':
    # now we are opening a new file with the help of with and writing on it
    # also we have included both read and write mode at the same time
    with open("hello2.txt", 'r+') as f:
        hello=f.read()
        for i in range(5):
             f.write("hey gbn \n")
        f.write(hello)

