class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        j,i = 0,1
        ans = 0
        while i < n:
            if prices[i] > prices[j]:
                ans = max(ans, prices[i] - prices[j])
            else:
                j = i
            i += 1
        return ans