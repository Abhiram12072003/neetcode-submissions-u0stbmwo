class Solution:
    # self.st = []
    def func(self, nums, i, n, xi):
        if i == n:
            if not xi:
                return
            else:
                self.st.append(xi[:])
                # print(self.st)
            return
        xi.append(nums[i])
        self.func(nums, i+1, n, xi)
        xi.pop()
        self.func(nums, i+1, n, xi)
        return
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        self.st = []
        self.func(nums, 0, n, [])
        ans = 0
        # print(self.st)
        for lis in self.st:
            xi = 0
            for i in lis:
                xi ^= i
            ans += xi
        return ans