class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xi = []
        answer = []
        def func(itr):
            if itr == len(nums):
                answer.append(xi[:])
                return
            
            xi.append(nums[itr])
            func(itr+1)
            xi.pop()
            func(itr+1)
        func(0)
        ans = 0
        for i in range(len(answer)):
            hi = 0
            for j in answer[i]:
                hi = hi^j
            ans += hi
        return ans