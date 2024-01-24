class Node:
    def __init__(self,val):
        self.next=None
        self.val=val
class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0
        

    def get(self, index: int) -> int:
        current=self.head
        i=0
        while i<index:
            if not current.next:
                return -1
            current=current.next
            i+=1
        if not current:
            return -1
        return current.val

        

    def addAtHead(self, val: int) -> None:
        newnode=Node(val)
        newnode.next=self.head
        self.head=newnode
        self.size+=1
        

    def addAtTail(self, val: int) -> None:
        newnode=Node(val)
        if self.head:
            current=self.head
            while current.next:
                current=current.next
            current.next=newnode
        else:
            self.head=newnode
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        newnode=Node(val)
        if index==0:
            newnode=Node(val)
            newnode.next=self.head
            self.head=newnode
            return None

        current=self.head
        i=0
        while i<index-1:
            if not current or not current.next:
                return -1
            current=current.next
            i+=1
        if not current:
            return -1
        if current and not current.next:
            current.next=newnode
            return None

        newnode.next=current.next
        current.next=newnode

        

    def deleteAtIndex(self, index: int) -> None:
        if index==0:
            self.head=self.head.next
            return None
        current=self.head
        i=0
        while i<index-1:
            if not current.next:
                return -1
            current=current.next
            i+=1
        if not current or not current.next:
            return -1
        elif not current.next.next:
            current.next=None
        else:
            current.next=current.next.next
        self.size-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)