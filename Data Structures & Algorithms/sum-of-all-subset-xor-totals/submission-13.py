class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        hs = 0
        for i in nums:
            hs = hs|i
        return hs*(1<<(n-1))