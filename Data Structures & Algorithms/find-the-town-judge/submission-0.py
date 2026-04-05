from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d1 = defaultdict(list)
        d2 = defaultdict(list)

        for p1, p2 in trust:
            d1[p2].append(p1)
            d2[p1].append(p2)

        for key in d1:
            if len(d1[key]) == n-1:
                if key not in d2:
                    return key
        
        return -1
