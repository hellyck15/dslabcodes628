class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp = self.head
        while temp:
            print(temp.data, "-->", end=" ")
            temp = temp.next

    def addnodebeg(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode
        newnode.prev = None

    def addnodeend(self, data):
        newnode = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newnode
        newnode.prev = temp

    def addnodepos(self, pos, data):
        newnode = Node(data)
        temp = self.head
        for i in range(1, pos - 1):
            temp = temp.next
        newnode.prev = temp
        newnode.next = temp.next
        temp.next.prev = newnode
        temp.next = newnode

    def deletebeg(self):
        self.head.next.prev = None
        self.head = self.head.next
        self.head.prev = None

    def deleteend(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None
        temp.prev = None

    def deletepos(self, pos):
        temp = self.head.next
        prev = self.head
        for i in range(1, pos - 1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next.prev = prev
        temp.next = None
        temp.prev = None


l1 = DLL()
ch = 1
while ch != 8:
    ch = int(input(
        'enter your choice \n1.Insert begin \n2.Insert at pos \n3.Insert End \n4.Delete begin \n5.Delete at pos \n6.Delete End \n7.display \n8.exit\n:  '))
    if ch == 1:
        ele = int(input('enter element to insert:'))
        l1.addnodebeg(ele)
    elif ch == 2:
        ele = int(input('enter element to insert:'))
        pos = int(input('Enter the position at which node to be inserted'))
        l1.addnodepos(pos, ele)
    elif ch == 3:
        ele = int(input('enter element to insert:'))
        l1.addnodeend(ele)
    elif ch == 4:
        l1.deletebeg()
    elif ch == 5:
        pos = int(input('Enter the position at which node to be deleted'))
        l1.deletepos(pos)
    elif ch == 6:
        l1.deleteend()
    elif ch == 7:
        l1.display()
