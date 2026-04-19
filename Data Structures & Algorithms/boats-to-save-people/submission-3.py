class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        x = max(people)
        count = [0]*(x+1)
        for p in people:
            count[p] += 1
        n = len(people)
        idx, i = 0, 1
        while idx < n:
            while count[i] == 0:
                i += 1
            count[i] -= 1
            people[idx] = i
            idx += 1
        
        res, i, j = 0, 0, n-1
        while i<=j:
            rem = limit - people[j]
            j -= 1
            res += 1
            if i<=j and rem>=people[i]:
                i += 1
        
        return res