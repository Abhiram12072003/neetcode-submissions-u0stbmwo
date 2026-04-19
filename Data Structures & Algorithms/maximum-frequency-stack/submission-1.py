class FreqStack:

    def __init__(self):
        self.maxCnt = 0
        self.st = {}
        self.cnt = {}

    def push(self, val: int) -> None:
        cnt = 1 + self.cnt.get(val,0)
        self.cnt[val] = cnt
        if cnt > self.maxCnt:
            self.maxCnt = cnt
            self.st[self.maxCnt] = []
        self.st[cnt].append(val)
        print(self.st)

    def pop(self) -> int:
        res = self.st[self.maxCnt].pop()
        self.cnt[res] -= 1
        if not self.st[self.maxCnt]:
            self.maxCnt -= 1
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()