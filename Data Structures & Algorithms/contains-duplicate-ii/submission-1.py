class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        mp = {}
        i = 0
        while i < n:
            if nums[i] in mp and i - mp[nums[i]]<=k:
                return True
            mp[nums[i]] = i
            i += 1
        return False