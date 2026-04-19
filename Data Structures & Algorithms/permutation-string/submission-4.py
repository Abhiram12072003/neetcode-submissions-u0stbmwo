class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        for i in s1:
            if i not in d:
                d[i] = 0
            d[i] += 1
        n = len(s2)
        d2 = {}
        m = len(s1)
        i, j = 0, 0
        print(d)
        while i<n:
            if s2[i] not in d2:
                d2[s2[i]] = 0
            d2[s2[i]] += 1
            # print(j, i)
            if i-j+1 >= m:
                print(d, d2)
                while j<i and (s2[j] not in d or d[s2[j]] != d2[s2[j]]):
                    d2[s2[j]] -= 1
                    j += 1
            if i-j+1 == m:
                f = True
                for x in d:
                    if x not in d2 or d[x] != d2[x]:
                        f = False
                if f == True:
                    return True
            i += 1
        return False