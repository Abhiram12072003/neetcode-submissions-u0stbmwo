class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        matchsticks = sorted(matchsticks, reverse = True)
        su = sum(matchsticks)

        if su%4 != 0 or matchsticks[0] > (su//4):
            return False

        target = su//4
        side = [0]*4

        def func(itr):
            if itr == len(matchsticks):
                return True
            st = set()
            for i in range(4):
                f = False
                if (matchsticks[itr] + side[i]) <= target and side[i] not in st:
                    st.add(side[i])
                    side[i] += matchsticks[itr]
                    if func(itr+1):
                        return True
                    side[i] -= matchsticks[itr]
            return False
        return func(0)