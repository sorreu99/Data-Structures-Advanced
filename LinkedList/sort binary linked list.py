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

    def sortbin(self):
        
        temp = self.head
        demo = temp.next
        prev=self.head
        while demo:
            if demo.data == 0:
                temp.next = demo.next
                demo.next = self.head
                self.head = demo
                demo = temp.next

            elif demo.data==1:
                demo = demo.next
                temp=temp.next


l1 = LinkedList()
l1.push(1)
l1.push(0)
l1.push(0)
l1.push(1)
l1.push(0)
l1.push(1)
l1.printlist()

l1.sortbin()
l1.printlist()
