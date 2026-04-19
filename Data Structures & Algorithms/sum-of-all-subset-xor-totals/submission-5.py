class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        xi = 2**n
        ans = 0
        for mask in range(1, xi):
            val = 0
            for i in range(n):
                if mask & (1<<i):
                    val ^= nums[i]
            ans += val
        return ans    