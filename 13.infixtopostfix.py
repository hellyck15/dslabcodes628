class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return "stack is empty"
        return self.stack.pop()

    def peak(self):
        return self.stack[-1]

    def display(self):
        print(self.stack)


operators = Stack()
output_string = ""
operands = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
precedence = {'^': 5, '*': 4, '/': 4, '+': 3, '-': 3, '(': 2, ')': 1}
input_string = input("enter infix notation: ")
for character in input_string:
    if character in operands:
        output_string += character
    elif operators.is_empty() or operators.peak() == '(':
        operators.push(character)
    elif character == "(":
        operators.push(character)
    elif character == ")":
        x = operators.pop()
        while x != "(":
            output_string += x
            x = operators.pop()
    elif precedence[operators.peak()] < precedence[character]:
        operators.push(character)
    elif precedence[operators.peak()] >= precedence[character]:
        output_string += operators.pop()
        operators.push(character)
    else:
        output_string += character
for _ in range(len(operators.stack)):
    output_string += operators.pop()
print(output_string)
