class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = 100000
        i, j, s = 0, 0, 0
        while i<n:
            s += nums[i]
            while j<=i and s >= target:
                ans = min(ans, i - j + 1)
                s -= nums[j]
                j += 1
            i += 1
        if s < target and j==0:
            return 0
        # print(n)
        return min(ans, n)