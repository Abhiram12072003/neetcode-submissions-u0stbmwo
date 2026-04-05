from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for p1, p2 in trust:
            d1[p2] += 1
            d2[p1] += 1

        for i in range(1, n+1):
            if d2[i] == 0 and d1[i] == n-1:
                return i
        return -1
