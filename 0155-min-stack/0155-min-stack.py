class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min)>0:
            self.min.append(min(val, self.min[-1]))
        else:
            self.min.append(val)

    def pop(self) -> None:
        z = self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        z = self.stack[-1]
        return z

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()