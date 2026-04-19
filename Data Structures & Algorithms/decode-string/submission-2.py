class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        st2 = []
        x = ""
        for i in s:
            if i.isdigit():
                x += i
            elif i == '[':
                st2.append(int(x))
                st.append(i) 
                x = ""                                                                                                                            ""
            elif i == ']':
                xi = ""
                while st and st[-1] != '[':
                    xi = st[-1] + xi
                    st.pop()
                if st2:
                    xi = st2[-1]*xi
                    st2.pop()
                st.pop()
                st.append(xi)
            else:
                st.append(i)
            print(st,st2)
        ans = ""
        while st:
            ans = st[-1] + ans
            st.pop()
        return ans