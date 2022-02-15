class node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def revrselink(self):
        prev = None
        temp = self.head
        dummy = self.head
        while temp:
            dummy = temp.next
            temp.next = prev
            prev = temp
            temp = dummy
            
        self.head= prev
        prev=None


l1 = LinkedList()
l1.push(6)
l1.push(5)
l1.push(4)
l1.push(3)
l1.push(2)
l1.push(1)
l1.printlist()
l1.revrselink()
l1.printlist()
