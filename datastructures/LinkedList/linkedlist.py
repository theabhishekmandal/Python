class Node:
    def __init__(self,a:int)->None:
        self.data=a
        self.next=None


class linkedlist:
    def __init__(self)->None:
        self.head=None

    def append(self,data:int)->None:
        if self.head is None:
            self.head=Node(data)
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=Node(data)

    def prepend(self,data:int)->None:
        if self.head is None:
            self.head=Node(data)
        else:
            temp=Node(data)
            temp.next=self.head
            self.head=temp

    def delete(self,data:int)->None:
        if self.head is None:
            return print('nothing to delete')
        elif self.head.data==data:
            save=self.head.data
            self.head=self.head.next
            return print(str(save))
        else:
            temp=self.head
            while temp.next is not None:
                if temp.next.data==data:
                    save=temp.next.data
                    temp.next=temp.next.next
                    return print(str(save))
                temp=temp.next
        return print("value not found")

    def addInMiddle(self,data:int,pos:int)->None:
        if pos==1:
                self.prepend(data)
        else:
            temp=self.head
            count=0
            while temp is not None:
                count+=1
                temp=temp.next
            if pos>count:
                print('appending in the end is possible and not in the middle')
                self.append(data)
            else:
                temp=self.head
                temp2=None
                i=0
                while temp.next is not None and i!=pos:
                    temp2=temp
                    temp=temp.next
                    i+=1
                temp2.next=Node(data)
                temp2.next.next=temp





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
    ob=linkedlist()
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



