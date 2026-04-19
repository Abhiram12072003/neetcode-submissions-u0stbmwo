class Solution:
    def func(self, nums, itr, xi, n):
        if itr == n:
            return

        for i in range(itr, n):
            if i!=itr and nums[i] == nums[i-1]:
                continue
            # print(itr, i)
            xi.append(nums[i])
            self.answer.append(xi[:])
            self.func(nums, i+1, xi, n)
            xi.pop()
        

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # lis = list(set(nums))
        self.answer = [[]]
        nums =sorted(nums)
        print(nums)
        self.func(nums, 0, [], len(nums))
        return self.answer