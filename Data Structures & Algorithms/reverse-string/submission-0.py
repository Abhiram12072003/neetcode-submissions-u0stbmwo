class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i1, i2 = 0, len(s)-1
        while(i1<i2):
            s[i1], s[i2] = s[i2], s[i1]
            i1 += 1
            i2 -= 1
        