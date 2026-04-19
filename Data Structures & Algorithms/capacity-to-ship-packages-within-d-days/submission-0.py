class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        s = 0
        for i in weights:
            s += i
        n = len(weights)
        l,h = max(weights), s
        while l<=h:
            m = (l+h)//2
            x = 0
            cnt = 1
            for i in weights:
                x += i
                if x>m:
                    x = i
                    cnt += 1
            if cnt <= days:
                h = m - 1
            else:
                l = m + 1
        return l