class Solution:
    def func(self, nums, itr, n, xi):
        if itr == n:
            if xi not in self.answer:
                self.answer.append(xi[:])
            return
        for i in range(itr, n):
            if i != itr and nums[i] == nums[i-1]:
                continue
            nums[itr], nums[i] = nums[i], nums[itr]
            xi.append(nums[itr])
            self.func(nums, itr+1, n, xi)
            xi.pop()
            nums[itr], nums[i] = nums[i], nums[itr]

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        nums = sorted(nums)
        self.func(nums, 0, len(nums), [])
        return self.answer