stack = []


def addele():
    a = int(input("elements to be inserted"))
    for i in range(0, a):
        n = int(input("add element"))
        stack.append(n)
    print(stack)


def delele():
    stack.pop()
    print(stack)


print("1 addele \n2 delele \n3 break")
ch = 1
while ch != 3:
    ch = int(input("enter your choice"))
    if ch == 1:
        addele()
    elif ch == 2:
        delele()
    elif ch == 3:
        break