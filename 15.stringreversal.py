stack = []
stack2 = []


def reverse():
    a = int(input("elements to be inserted"))
    for i in range(0, a):
        n = int(input("add element"))
        stack.append(n)
    print(stack)
    for i in range(0, len(stack)):
        n = stack.pop()
        stack2.append(n)
    print(stack2)


reverse()