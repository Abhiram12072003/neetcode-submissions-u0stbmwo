class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        mp = {}
        s = set()
        i,j = 0,0
        while i < n:
            if i-j > k:
                s.remove(nums[j])
                j += 1
            if nums[i] in s:
                return True
            s.add(nums[i])
            i += 1
        return False