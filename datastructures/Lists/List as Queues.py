from collections import deque

if __name__ == '__main__':
    '''Lists can also be used as queue, but they are not efficient for this purpose.
       While appends and pop from the end of the lists are fast but doing inserts and
       pop from the front is slow. It requires to shift the elements by one position. 
       For this purpose we use deque from collections'''

    arr = deque([])
    while True:
        print('''Enter your choice
                            1. For adding a value
                            2. For deleting a value
                            3. seeing the top value\n''')
        n = input().strip()
        if n == '1':
            n = input('enter how many elements\n')
            arr.extend(list(map(int, input().strip().split(' '))))
            print(arr)
        elif n == '2':
            if len(arr) is 0:
                print("No element exists")
            else:
                print('how many elements to delete')
                n = int(input().strip())
                if n > len(arr):
                    print('Deleted elements are')
                    print(arr)
                    arr.clear()
                else:
                    for i in range(n):
                        print(arr.popleft(), end = ' ')
        elif n == '3':
            if len(arr) is 0:
                print('No elements to show')
            else:
                pop = arr.popleft()
                print(pop)
                arr.appendleft(pop)

        if input('Do you want to continue y or n ?\n').strip() is not 'y':
            break
