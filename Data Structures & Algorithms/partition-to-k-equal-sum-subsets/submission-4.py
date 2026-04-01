class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        su = sum(nums)
        nums = sorted(nums, reverse = True)
        if su%k != 0 or nums[0]>(su//k):
            return False
        side = [0]*k
        su = su//k
        def func(itr):
            if itr == len(nums):
                return True
            st = set()
            for i in range(k):
                if side[i] + nums[itr] <= su and side[i] not in st:
                    st.add(side[i])
                    side[i] += nums[itr]
                    if func(itr+1):
                        return True
                    side[i] -= nums[itr]
            return False
        return func(0)
                