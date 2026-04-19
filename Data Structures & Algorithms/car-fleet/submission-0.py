class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [(p,s) for p,s in zip(position,speed)]
        st = []
        for p,s in sorted(ps)[::-1]:
            k = (target-p)/s
            st.append(k)
            if len(st)>=2 and st[-2]>=st[-1]:
                st.pop()
        return len(st)