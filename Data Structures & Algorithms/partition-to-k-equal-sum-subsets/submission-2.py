class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums = sorted(nums, reverse = True)
        ksum = [0]*k        
        su = sum(nums)

        if su % k != 0 or nums[0] > (su//k):
            return False
            
        su = su//k
        # print(nums, su)
        
        def func(itr):
            if itr == len(nums):
                for i in range(1,k):
                    if ksum[i-1] != ksum[i]:
                        return False
                return True
            
            for i in range(k):
                if ksum[i] + nums[itr] <= su:
                    ksum[i] += nums[itr]
                    if func(itr+1):
                        return True
                    ksum[i] -= nums[itr]
                
                if ksum[i] == 0:
                    break
            return False

        return func(0)