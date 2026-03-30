class MinStack:

    def __init__(self):
        self.array = []
        self.MinStack =[]
        
    def push(self, val: int) -> None:
        self.array.append(val)
        if not self.MinStack or val <= self.MinStack[-1]:
            self.MinStack.append(val)

    def pop(self) -> None:
        if self.MinStack[-1] == self.array[-1]:
            self.MinStack.pop()
        self.array.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]
        
