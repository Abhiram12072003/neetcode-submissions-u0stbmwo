class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lis = []
        
        for no,fr,to in trips:
            lis.append([fr,to,no])
        
        lis.sort()
        n = len(lis)
        cp, i = 0, 0
        prev = None
        print(lis)
        while i < n:
            if i == 0:
                cp = lis[i][-1]
                prev = lis[i]
            elif prev[0] < lis[i][0] < prev[1]:
                cp += lis[i][-1]
                prev = [min(prev[0],lis[i][0]), max(prev[1],lis[i][1])]
            else:
                cp = lis[i][-1]
                prev = lis[i]
            i += 1
            if cp > capacity:
                return False
        return True