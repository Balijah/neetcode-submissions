class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        return None

    def push(self, val: int) -> None:
        self.stack.append(val)
        for i in range(len(self.minstack)):
            if val < self.minstack[i]:
                self.minstack.append(self.minstack[i])
            elif self.minstack: 
                continue
        return None    

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        for i in self.stack:
            return min(self.stack)
        
         
