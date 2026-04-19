class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i = 1
        ans = 0
        x = []
        mx = 0
        for i in range(n-1, -1,-1):
            mx = max(mx, prices[i])
            x.append(mx)
        x = x[::-1]
        print(x)
        ans = 0
        for i in range(n-1):
            if x[i+1]>prices[i]:
                ans = max(ans, (x[i+1] - prices[i]))
        return ans
            