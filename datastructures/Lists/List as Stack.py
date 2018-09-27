if __name__ == '__main__':
    arr = []
    while True:
        print('''Enter your choice
                    1. For adding a value
                    2. For deleting a value
                    3. seeing the top value\n''')
        n = input().strip()
        if n == '1':
            print('how many elements you want to enter ')
            n = int(input().strip())
            arr[len(arr):] = list(map(int, input().strip().split(' ')))
            print(arr)
        elif n == '2':
            print('how many elements you want to delete')
            n = int(input().strip())
            if len(arr) is 0:
                print('No elements to delete')
                exit(0)
            elif n > len(arr):
                print('Deleted elements are')
                print(arr)
                arr.clear()
            else:
                blah = arr[len(arr) - n:]
                print('Deleted elements are')
                print(blah)
                arr = arr[:len(arr) - n]
        elif n == '3':
            if len(arr) is 0:
                print('No elements to show')
            else:
                print(arr[len(arr) - 1])
        print('Do you want to continue y or n?')
        out = input().strip()
        if out is 'n':
            break

