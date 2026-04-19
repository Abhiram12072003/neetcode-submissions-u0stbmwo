class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        d1 = {}
        for i in s1:
            d1[i] = 1 + d1.get(i,0)
        i, j = 0, 0
        jk = len(d1)
        d2 = {}
        while j<n2:
            print(i,j)
            d2[s2[j]] = 1 + d2.get(s2[j],0)
            print(d2)
            if j-i+1>=n1:
                while i<=j and (s2[i] not in d1 or d1[s2[i]]<d2[s2[i]]):
                    d2[s2[i]] -= 1
                    i += 1
                fnd = False
                cn = 0
                for h in d1:
                    if h not in d2 or d2[h] != d1[h]:
                        fnd = True
                for h in d2:
                    if d2[h] != 0:
                        cn += 1
                if fnd == False and cn == jk:
                    return True
            j += 1

        return False