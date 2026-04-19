class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        i, j = 0, n-1
        mod = 1000000007
        ans = 0
        while i<n:
            while i<=j and nums[i] + nums[j] > target:
                j -= 1
            if i<=j:
                ans += pow(2,j-i,mod)
                ans %= mod
            i += 1
        return ans