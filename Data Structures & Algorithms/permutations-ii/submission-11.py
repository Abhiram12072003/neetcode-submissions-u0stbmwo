class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        vis = [False]*n
        nums = sorted(nums)
        xi = []
        ans = []
        def func():
            if len(xi) == len(nums):
                ans.append(xi[:])
                return

            for i in range(n):
                if vis[i]:
                    continue
                
                if i and nums[i] == nums[i-1] and not vis[i-1]:
                    continue
                
                xi.append(nums[i])
                vis[i] = True
                func()
                vis[i] = False
                xi.pop()
        
        func()
                
        # return list(ans)
        return ans
            