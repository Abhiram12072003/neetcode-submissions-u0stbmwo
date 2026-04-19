class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        i = 0
        ans = []
        while i < n-3:
            j = i + 1
            while j < n-2:
                p1, p2 = j+1, n-1
                while p1<p2:
                    s = nums[i] + nums[j] + nums[p1] + nums[p2]
                    if s == target:
                        ans.append([nums[i],nums[j],nums[p1],nums[p2]])
                        p1 += 1
                        p2 -= 1
                        while p1<p2 and nums[p2] == nums[p2+1]:
                            p2 -= 1
                    elif s < target:
                        p1 += 1
                    else:
                        p2 -= 1
                j += 1
                while j<n-2 and nums[j] == nums[j-1]:
                    j += 1
            i += 1
            while i<n-3 and nums[i] == nums[i-1]:
                i += 1
        return ans