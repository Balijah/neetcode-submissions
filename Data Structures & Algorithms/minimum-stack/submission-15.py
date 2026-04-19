class MinStack:

    def __init__(self):
        self.res = []
        

    def push(self, val: int) -> None:
        if not self.res:
            self.res.append((val,val))
        elif val < self.res[-1][1]:
            self.res.append((val,val))
        else:
            self.res.append((val, self.res[-1][1]))

    def pop(self) -> None:
        self.res.pop()

    def top(self) -> int:
        return self.res[-1][0]

    def getMin(self) -> int:
        return self.res[-1][1]
