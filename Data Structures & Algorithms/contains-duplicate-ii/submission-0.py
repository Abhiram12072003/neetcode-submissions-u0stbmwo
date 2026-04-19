class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        i, j = 0, 0
        for i in range(n):
            for j in range(i+1, n):
                if j - i > k:
                    break
                if nums[i] == nums[j]:
                    return True
        return False