class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i,num in enumerate(numbers):
            if target - num in d:
                return [d[target-num]+1, i+1]
            d[num] = i
        return [-1, -1]