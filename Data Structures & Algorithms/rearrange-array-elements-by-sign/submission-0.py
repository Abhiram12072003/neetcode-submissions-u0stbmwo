class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l1, l2 = [], []
        for i in nums:
            if i>0:
                l1.append(i)
            else:
                l2.append(i)
        n = len(nums)
        i, j = 0, 0
        cnt = 0
        x = []
        while cnt < n:
            if cnt % 2 == 0:
                x.append(l1[i])
                i += 1
            else:
                x.append(l2[j])
                j += 1
            cnt += 1
        return x