class MinStack:

    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


s = MinStack()
s.push(100)
s.push(12312)
s.push(1)
print(s.top())
print(s.getMin())


