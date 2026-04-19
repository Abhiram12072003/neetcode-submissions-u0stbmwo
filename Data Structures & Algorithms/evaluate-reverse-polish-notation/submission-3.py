class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i not in ("+", "-", "*", "/"):
                st.append(int(i))
            else:
                p1 = st.pop()
                p2 = st.pop()
                if i == "+":
                    st.append(p1+p2)
                elif i == "/":
                    st.append(int(float(p2)/p1))
                elif i == "-":
                    st.append(p2-p1)
                else:
                    st.append(p1*p2)
            print(st)
        return st[0]