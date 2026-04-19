class Solution:
    def generate(self, nums, itr, n, xi):
        if itr == n:
            self.ans.append(xi[:])
            return
        xi.append(nums[itr])
        self.generate(nums, itr+1, n, xi)
        xi.pop()
        self.generate(nums, itr+1, n, xi)
        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.generate(nums, 0, len(nums), [])
        return self.ans  