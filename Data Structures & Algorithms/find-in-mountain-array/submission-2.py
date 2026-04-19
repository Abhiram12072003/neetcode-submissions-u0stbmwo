class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def binary(l,h):
            if mountainArr.get(l)<=mountainArr.get(h):
                # print("dsf", l,h)
                while l<=h:
                    m = (l+h)//2
                    if mountainArr.get(m) == target:
                        while m>=0 and mountainArr.get(m) == target:
                            m -= 1
                        return m+1
                    elif mountainArr.get(m)>target:
                        h = m - 1
                    else:
                        l = m + 1
            else:
                # print("xzc")
                while l<=h:
                    m = (l+h)//2
                    if mountainArr.get(m) == target:
                        while m>=0 and mountainArr.get(m) == target:
                            m -= 1
                        return m+1
                    elif mountainArr.get(m)>target:
                        l = m + 1
                    else:
                        h = m - 1
            return -1
        n = mountainArr.length()
        l, h = 0, n-1
        xi = 0
        while l<=h:
            m = (l+h)//2
            if m<n-1 and mountainArr.get(m)>mountainArr.get(m+1):
                xi = m
                h = m - 1
            else:
                l = m + 1
        # print(xi)
        x1 = binary(0,xi)
        x2 = binary(xi+1, n-1)
        if x1!=-1:
            return x1
        return x2