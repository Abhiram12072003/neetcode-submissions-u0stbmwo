class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in nums:
            ans |= i
        ans = ans << (n-1)
        return ans    
