class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        start, end = 0, n
        ans = []
        def func(nums, start, end):
            if start == end:
               ans.append(nums[:])
               return
            for i in range(start, end):
                nums[i], nums[start] = nums[start], nums[i]
                # print(start, i, nums)
                func(nums, start+1, end)
                nums[i], nums[start] = nums[start], nums[i]
            return
        func(nums, 0, n)
        return ans