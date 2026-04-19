class Solution:
    def func(self, lis, itr, left, right, top, bottom, leng):
        if len(lis) == itr:
            return True
        # fg = True
        l = r = t = b = False
        if left + lis[itr] <= leng:
            # fg = False
            l = self.func(lis, itr+1, left+lis[itr], right, top, bottom, leng)
        if right + lis[itr] <= leng:
            # fg = False
            r = self.func(lis, itr+1, left, right+lis[itr], top, bottom, leng)
        if top + lis[itr] <= leng:
            # fg = False
            t = self.func(lis, itr+1, left, right, top+lis[itr], bottom, leng)
        if bottom + lis[itr] <= leng:
            # fg = False
            b = self.func(lis, itr+1, left, right, top, bottom+lis[itr], leng)
        
        return l or r or t or b
         
    def makesquare(self, matchsticks: List[int]) -> bool:
        lis = sorted(matchsticks, reverse = True)
        xi = lis[0]
        cnt = 0
        n = len(lis)
        s = sum(lis)

        if s%4 != 0:
            return False
        
        s = s//4
        self.vis = [False]*len(lis)
        return self.func(lis, 0, 0, 0, 0, 0, s)

        