class Node:
    def init(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CDLL:
    def init(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp = self.head
        while temp != self.head:
            print(temp.data, "-->", end=" ")
            temp = temp.next
        print(temp.data)

    def addnodebeg(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
            newnode.prev = self.head
        else:

            temp = self.head
            temp.prev.next = newnode
            newnode.prev = temp.prev
            newnode.next = temp
            temp = newnode

    def addnodeend(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
            newnode.prev = self.head
        else:

            temp = self.head
            temp.prev.next = newnode
            newnode.next = temp
            newnode.prev = temp.prev

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
        if self.head is None:
            print('no elements present')
        else:
            temp = self.head
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp = temp.next

    def deleteend(self):
        if self.head is None:
            print('no elements present')
        else:
            temp = self.head
            temp.prev = temp.prev.prev
            temp.prev.prev.next = temp

    def deletepos(self, pos):
        temp = self.head.next
        before = self.head
        for i in range(1, pos - 1):
            temp = temp.next
            before = before.next
        before.next = temp.next
        temp.next.prev = before
        temp.next = None
        temp.prev = None


l1 = CDLL()
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