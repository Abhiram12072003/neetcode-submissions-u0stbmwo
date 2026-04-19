class Solution:
    def trap(self, height: List[int]) -> int:
        x = []
        h = 0
        for i in height[::-1]:
            h = max(i,h)
            x.append(h)
        x = x[::-1]
        n = len(height)
        ans = 0
        h = 0
        # print(x)
        for i in range(n):
            h = max(h, height[i])
            ans += (min(h,x[i]) - height[i])
        return ans