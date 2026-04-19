class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        def func(i, s):
            if i == n:
                return s
            # print(nums[:i+1])
            return func(i+1,nums[i]^s) + func(i+1, s)
        
        return func(0, 0)