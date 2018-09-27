def partition(arr:list,p:int,q:int) ->int:
    pindex=p
    pivot=arr[q]
    for i in range(p,q):
        if arr[i]<pivot:
            arr[i],arr[pindex]=arr[pindex],arr[i]
            pindex+=1
    arr[pindex],arr[q]=arr[q],arr[pindex]
    return pindex


def QuickSort(arr:list,p:int,r:int) ->None:
    if p<r:
        q=partition(arr,p,r)
        QuickSort(arr,p,q-1)
        QuickSort(arr,q+1,r)


if __name__ == '__main__':
    print("enter the size of the array")
    n = int(input().strip())
    print("enter the elements ")
    arr = [int(i) for i in input().strip().split(' ')]
    QuickSort(arr, 0, len(arr) - 1)
    print(" ".join(str(i) for i in arr))