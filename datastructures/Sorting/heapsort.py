def heapify(arr, i, length):
	l = 2 * i + 1
	r = 2 * i + 2
	largest = i
	if l < length and arr[l] > arr[largest]:
		largest = l
	if r < length and arr[r] > arr[largest]:
		largest = r
	if i != largest:
		arr[largest], arr[i] = arr[i], arr[largest]
		heapify(arr, largest, length)

def buildmaxheap(arr, lastindex):
	for i in range(lastindex // 2, 0, -1):
		heapify(arr, i, len(arr))

def heapsort(arr):
	buildmaxheap(arr, len(arr) - 1)
	for i in range(len(arr) - 1, 0, -1):
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, 0, i)

if __name__ == '__main__':
	arr = list(map(int, input().strip().split(' ')))
	heapsort(arr)
	print(arr)