class Solution:
    def reorganizeString(self, s: str) -> str:
        lis = []
        ans, i, n = "", 0, len(s)
        d = {}
        
        while i < n:
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
            i += 1
        
        for key in d:
            heapq.heappush(lis, [-d[key],key])

        prev = None
        cnt = 0
        while lis:
            tp = heapq.heappop(lis)
            ans += tp[1]
            tp[0] += 1
            if prev and prev[0] != 0:
                heapq.heappush(lis, prev)
            if tp[0] != 0:
                prev = tp
            else:
                prev = None
        if prev:
            return ""

        return ans