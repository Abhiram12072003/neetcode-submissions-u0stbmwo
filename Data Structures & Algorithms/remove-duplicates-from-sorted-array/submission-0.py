class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        n = len(nums)
        cnt = 1
        while j < n:
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                cnt += 1
                j += 1
        return cnt