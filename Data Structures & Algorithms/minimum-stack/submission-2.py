class MinStack:

    def __init__(self):
        self.st = []
        self.mn = 0         

    def push(self, val: int) -> None:
        if len(self.st) == 0:
            self.mn = val
            self.st.append(0)
        else:
            self.st.append(val-self.mn)
            if self.mn > val:
                self.mn = val

    def pop(self) -> None:
        x = self.st[-1]
        if x < 0:
            self.mn = self.mn - x
        self.st.pop()
    def top(self) -> int:
        tp = self.st[-1]
        if tp>0:
            return tp+self.mn
        else:
            return self.mn
        # return self.st[-1]+self.mn

    def getMin(self) -> int:
        return self.mn