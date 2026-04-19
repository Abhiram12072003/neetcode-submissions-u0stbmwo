class MedianFinder:

    def __init__(self):
        self.st = []
        self.st2 = []

    def addNum(self, num: int) -> None:
        if self.st and (-self.st[0]) > num:
            heapq.heappush(self.st, -num)
        else:
            heapq.heappush(self.st2, num)
        
        if len(self.st) > len(self.st2) + 1:
            heapq.heappush(self.st2, -heapq.heappop(self.st))
        elif len(self.st2) > len(self.st) + 1:
            heapq.heappush(self.st, -heapq.heappop(self.st2))
    
    def findMedian(self) -> float:
        if len(self.st) > len(self.st2):
            return -self.st[0]/1.0
        elif len(self.st) < len(self.st2):
            return self.st2[0]/1.0
        else:
            return (-self.st[0]+self.st2[0])/2.0
        
        