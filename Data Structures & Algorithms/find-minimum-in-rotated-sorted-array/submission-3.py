class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, h = 1, n - 2
        while l<=h:
            m = (l+h)//2
            if nums[m-1]>=nums[m] and nums[m]<=nums[m+1]:
                return nums[m]
            elif nums[0]>nums[m]:
                h = m - 1
            else:
                l = m + 1
        return min(nums[0], nums[n-1])