class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        i,j = 0, 0
        idx = 0
        mx = 0
        ans = []
        while j<k:
            if mx<nums[j]:
                mx = nums[j]
                idx = j
                i = idx
            j += 1
        ans.append(nums[i])
        while j<n:
            if mx<nums[j]:
                mx = nums[j]
                i = j
            else:
                if i <= j-k:
                    mx = nums[j]
                    idx = i
                    i = j-k+1
                    while i<=j:
                        if mx<nums[i]:
                            mx = nums[i]
                            idx = i
                        i += 1
                    i = idx
            j += 1
            ans.append(mx)
        return ans
