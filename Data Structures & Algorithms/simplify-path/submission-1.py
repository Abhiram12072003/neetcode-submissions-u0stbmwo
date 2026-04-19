class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        ans = ""        
        st = []
        x = path.split('/')
        for i in x:
            if i == "":
                continue
            if i == "..":
                if st:
                    st.pop()
            elif i != '.':
                st.append(i)
        return "/" + "/".join(st)