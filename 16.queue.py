class Queue:

    def __init__(self):
        self.elements = []

    def enqueue(self, data):
        self.elements.append(data)
        return data

    def dequeue(self):
        return self.elements.pop(0)

    def rear(self):
        if len(self.elements)==0:
            print("No elements present")
        else:
            print(self.elements[-1])

    def front(self):
        if len(self.elements) == 0:
            print("No elements present")
        else:
            print(self.elements[0])


    def isempty(self):
        if len(self.elements) == 0:
            print("True")
        else:
            print("false")
    def display(self):
        print(self.elements)




if __name__ == '__main__':
    Q= Queue()
    ch=1
    while ch!=7:
        print("1.enqueue\n2.dequeue\n3.rear\n4.front\n5.isempty\n6.display\n7.exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
            n=int(input("size of queue"))
            for i in range(n):
                data=input("enter data to insert in queue:")
                Q.enqueue(data)
        elif ch==2:
            ans=1
            while ans!=0:
                ans = int(input("want to dequeue elements?(yes:1/no:0)"))
                if ans==1:
                    Q.dequeue()
                else:
                    break
        elif ch==3:
            Q.rear()
        elif ch==4:
            Q.front()
        elif ch==5:
            Q.isempty()
        elif ch==6:
            Q.display()
        else:
            break