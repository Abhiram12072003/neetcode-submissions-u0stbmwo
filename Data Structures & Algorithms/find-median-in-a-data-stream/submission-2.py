class MedianFinder:

    def __init__(self):
        self.st = []

    def addNum(self, num: int) -> None:
        n = len(self.st)
        i = 0
        # print(self.st)
        while i < n and self.st[i] < num:
            i += 1
        if i == n:
            self.st.append(num)
        else:
            tp = self.st[n-1]
            cs = n-1
            while i != cs:
                self.st[cs] = self.st[cs-1]
                cs -= 1
            # print("num:",num, cs)
            self.st[i] = num
            self.st.append(tp)
    def findMedian(self) -> float:
        print("ms",self.st)
        mid = len(self.st)//2
        if len(self.st)%2 == 0:
            return (self.st[mid] + self.st[mid - 1])/2.0
        else:
            return self.st[mid]
    