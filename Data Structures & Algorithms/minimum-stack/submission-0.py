class MinStack:

    def __init__(self):
        self.minVal = None
        self.stack =[]
        

    def push(self, val: int) -> None:
        if self.minVal is None:
            self.minVal = val
        else:
            self.minVal = min(self.minVal, val)
        
        self.stack.append((val, self.minVal))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
