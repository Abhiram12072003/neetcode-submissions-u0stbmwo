class Solution:
    def func(self, n, xi, itr, st):
        
        if xi.count('(') == n:
            st2 = st[:]
            while st2:
                xi += ')'
                st2.pop()
            self.answer.append(xi)
            return
        
        # print(itr, st)
        st.append('(')

        st2 = st[:]
        self.func(n, xi+'(', itr+1, st)
        st2.pop()
        
        if st2:
            # if itr == 1:
            st2.pop()
            xi = xi + ')'
            # print(st,xi)
            self.func(n, xi, itr, st2)

    def generateParenthesis(self, n: int) -> List[str]:
        self.answer = []
        st = ['(']
        self.func(n, '(', 1, st)
        return self.answer
