class stack:
    def __init__(self):
        self.a = []

    def push(self, b):
        self.a.append(b)

    def pop(self):
        self.a.pop()

    def top(self):
        return self.a[-1]


stack1 = stack()
stack1.push(1)
stack1.pop()
stack1.push(3)
stack1.push(1)

print(stack1.top())
