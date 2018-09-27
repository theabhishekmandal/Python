def insertion(arr:list) -> None:
    for i in range(1,len(arr)):
        j=i-1
        key=arr[i]
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

    
if __name__ == '__main__':
    print("enter the size of the array")
    n=int(input().strip())
    print("enter the elements ")
    arr=[int(i) for i in input().strip().split(' ')]


    insertion(arr)
    print(" ".join(str(i) for i in arr))