if __name__ == '__main__':
    '''Example of two d matrix'''
    matrix = []
    print('Enter how many rows and columns')
    n, m = [int(i) for i in input().strip().split(' ')]
    for _ in range(n):
        matrix.append(list(map(int, input().strip().split(' '))))
    print(matrix)