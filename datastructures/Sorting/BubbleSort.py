# this program is the python implementation of bubble sort
def bubblesort(a:list)->list:
    for i in range (0,len(a)-1):
        for j in range (0,len(a)-i-1):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


if __name__ == '__main__':
    n=int(input("enter the size of the array").strip())
    array=[]
    print("enter the elements of the array seperated by enter")
    for i in range (n):
        array.append(int(input().strip()))
    array=bubblesort(array)
    print(" ".join(str(i)for i in array))
