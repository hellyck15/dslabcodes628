class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next

    def insert_beg(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_end(self, data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

    def insert_pos(self, pos, data):
        np = Node(data)
        temp = self.head
        for i in range(pos - 1):
            temp = temp.next
        np.data = data
        np.next = temp.next
        temp.next = np

    def delete_beg(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def delete_end(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def delete_pos(self, pos):
        prev = self.head
        temp = self.head.next
        for i in range(1, pos - 1):
            prev = prev.next
            temp = temp.next
        prev.next = temp.next


l1 = SLL()
ch = 1
while ch != 11:
    ch = int(input(
        'enter your choice \n1.Insert begin \n2.Insert End  \n3.Insert Pos \n4.Delete begin \n5.Delete End \n6.Delete pos \n7.display \n11.exit\n:  '))
    if ch == 1:
        ele = int(input('enter element to insert:'))
        l1.insert_beg(ele)
    elif ch == 2:
        ele = int(input('enter element to insert:'))
        l1.insert_end(ele)
    elif ch == 3:
        ele = int(input("enter element to insert:"))
        pos = int(input('Enter the position at which node to be inserted'))
        l1.insert_pos(pos, ele)
    elif ch == 4:
        l1.delete_beg()
    elif ch == 5:
        l1.delete_end()
    elif ch == 6:
        pos = int(input('Enter the position at which node to be deleted'))
        l1.delete_pos(pos)
    elif ch == 7:
        l1.display()
