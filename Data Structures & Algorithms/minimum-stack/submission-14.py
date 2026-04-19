class MinStack:

    def __init__(self):
        self.minstack = []
        self.res = []
        return None
        

    def push(self, val: int) -> None:
        self.res.append(val)
        if not self.minstack:
            self.minstack.append(val)
        elif val < self.minstack[-1]:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        self.res.pop()
        if self.minstack:
            self.minstack.pop()
        return None

    def top(self) -> int:
        return self.res[-1]

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        return None
