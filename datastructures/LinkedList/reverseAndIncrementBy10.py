import linkedlist

class hello(linkedlist.linkedlist, linkedlist.Node):
	def __init__(self):
		linkedlist.linkedlist.__init__(self)

	def incrementandshow(self) -> None:
		if self.head is None:
			print('increment not possible')
			return
				
		self.show()        
		prev = None
		current = self.head
		nex = None
		count = 0
		while current is not None:
			nex = current.next
			current.next = prev
			prev = current
			current = nex
			count += 1
		self.head = prev
		temp = self.head.next
		carry = 1
		while temp.next is not None:
			save = temp.data + carry
			temp.data = save % 10
			carry = save // 10
			temp = temp.next
		if carry is not 0:
			temp.next = Node(carry)

		prev = None
		current = self.head
		nex = None
		while current is not None:
			nex = current.next
			current.next = prev
			prev = current
			current = nex
		self.head = prev
		self.show()

if __name__ == '__main__':
	ob = hello()
	arr = list(map(int, input('enter array of numbers to form linked list \n').strip().split(' ')))
	for i in arr:
		ob.append(i)
	ob.incrementandshow()
