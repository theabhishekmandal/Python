class sl:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    class Node:
        def __init__(self, data, nextnode=None) -> None:
            self.data = data
            self.next = nextnode

        def __str__(self):
            return f"[{self.data}]-->"

    def append(self, data) -> None:
        last = self.tail
        node = self.Node(data)
        self.tail = node
        if last is None:
            self.head = node
        else:
            last.next = node
        self.size += 1

    def prepend(self, data) -> None:
        first = self.head
        node = self.Node(data, first)
        self.head = node
        if first is None:
            self.tail = node
        self.size += 1

    def delete(self, data:int) -> None:
        if self.head is None:
            return print('nothing to delete')
        elif self.head.data == data:
            save = self.head.data
            self.head = self.head.next
            return print(str(save))
        else:
            temp = self.head
            while temp.next is not None:
                if temp.next.data == data:
                    save = temp.next.data
                    temp.next = temp.next.next
                    return print(str(save))
                temp = temp.next
        return print("value not found")

    def addInMiddle(self, data, pos) -> None:
        if pos == 1:
                self.prepend(data)
        else:
            temp = self.head
            count = 0
            while temp is not None:
                count += 1
                temp = temp.next
            if pos > count:
                print('appending in the end is possible and not in the middle')
                self.append(data)
            else:
                temp = self.head
                temp2 = None
                i = 0
                while temp.next is not None and i != pos:
                    temp2 = temp
                    temp = temp.next
                    i += 1
                temp2.next = self.Node(data)
                temp2.next.next = temp

    def show(self)->None:
        temp=self.head
        if temp is None:
            print("Nothing to show")
            return
        while temp is not None:
            print(temp.data,'-->',end='')
            temp=temp.next
        print()


if __name__ == '__main__':
    ob = sl()
    ob.append(10)
    ob.append(20)
    ob.append(30)
    ob.append(40)
    ob.show()
    ob.prepend(13)
    ob.show()
    ob.delete(50)
    ob.show()
    ob.addInMiddle(4000,4)
    ob.show()



