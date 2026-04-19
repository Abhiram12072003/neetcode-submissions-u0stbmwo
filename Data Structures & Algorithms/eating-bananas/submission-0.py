class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high = 1, max(piles)
        n = len(piles)
        while low<=high:
            m = (low+high)//2
            x = 0
            i = 0
            while i<n:
                x += math.ceil(piles[i]/m)
                i += 1
            # print(m, x, h)
            if x<=h:
                high = m - 1
            else:
                low = m + 1
        return low