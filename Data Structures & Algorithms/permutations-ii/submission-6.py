class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        # nums = sorted(nums)
        def func(itr):
            if itr == n:
                if nums not in ans:
                    ans.append(nums[:])
                    return
            for i in range(itr, n):
                # if i != itr and nums[i] == nums[i-1]:
                #     continue
                nums[i], nums[itr] = nums[itr], nums[i]
                func(itr+1)
                nums[i], nums[itr] = nums[itr], nums[i]
        func(0)
        return ans
            