class node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def push(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode

    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next

    def MiddleElement(self):

        temp=self.head
        mid=self.head
        count=0
        while temp:
            if count&1 :
                mid=mid.next
            count+=1
            temp=temp.next
        if mid!=None:
            print()
            print(mid.data)



l1=LinkedList()
l1.push(1)
l1.push(0)
l1.push(0)
l1.push(1)
l1.push(0)
l1.push(1)
l1.printlist()
l1.MiddleElement()

