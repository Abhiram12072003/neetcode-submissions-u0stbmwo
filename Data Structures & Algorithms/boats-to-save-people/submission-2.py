class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        arr = sorted(people)
        ans = 0
        s = 0
        d = {}
        n = len(arr)
        i,j = 0, len(arr) - 1
        while i<j:
            if arr[i] + arr[j] <= limit:
                d[i] = True
                d[j] = True
                i += 1
                j -= 1
                ans += 1
            elif arr[i] + arr[j] > limit:
                j -= 1
        i = 0
        while i <n:
            if i not in d:
                ans += 1
            i +=1
        return ans