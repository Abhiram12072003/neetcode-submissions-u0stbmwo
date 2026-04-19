class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,h = 0, n-1
        while l<=h:
            m = (l+h)//2
            if nums[m]==target:
                return m
            elif nums[l]<=nums[m]:
                if target<nums[m] and target>=nums[l]:
                    h = m - 1
                else:
                    l = m + 1
            else:
                if nums[m]<=target and nums[h]>=target:
                    l = m + 1
                else:
                    h = m - 1
        return -1
