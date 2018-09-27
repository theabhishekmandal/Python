from sys import maxsize


def MergeSort(arr:list,p:int,r:int) -> None:
    if p<r:
        q=p+(r-p)//2
        MergeSort(arr,p,q)
        MergeSort(arr,q+1,r)
        Merge(arr,p,q,r)


def Merge(arr:list,p:int,q:int,r:int) ->None:
    n1=q-p+1
    n2=r-q
    one=[arr[p+i] for i in range(n1)]
    two=[arr[q+1+i] for i in range(n2)]
    one.append(maxsize)
    two.append(maxsize)
    i=0
    j=0
    for k in range(p,r+1):
        if one[i]<two[j]:
            arr[k]=one[i]
            i+=1
        elif two[j]<one[i]:
            arr[k]=two[j]
            j+=1


if __name__ == '__main__':
    print("enter the size of the array")
    n = int(input().strip())
    print("enter the elements ")
    arr = [int(i) for i in input().strip().split(' ')]

    MergeSort(arr,0,len(arr)-1)
    print(" ".join(str(i) for i in arr))