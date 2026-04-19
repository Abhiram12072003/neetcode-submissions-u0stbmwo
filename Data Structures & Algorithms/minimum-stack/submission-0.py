class MinStack:

    def __init__(self):
        self.st = []
        self.st2 = []         

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.st2) == 0:
            self.st2.append(val)
        else:
            self.st2.append(min(val,self.st2[-1]))

    def pop(self) -> None:
        x = self.st[-1]
        self.st.pop()
        self.st2.pop()
        return x

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.st2[-1]