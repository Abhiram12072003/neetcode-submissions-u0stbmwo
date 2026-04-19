class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        n2 = len(matrix[0])
        l1, h1 = 0, n-1
        while l1<=h1:
            m1 = (l1+h1)//2
            if target > matrix[m1][-1]:
                l1 = m1 + 1
            elif target < matrix[m1][0]:
                h1 = m1 - 1
            else:
                l2, h2 = 0, n2-1
                while l2<=h2:
                    m = (l2+h2)//2
                    if matrix[m1][m] == target:
                        return True
                    elif matrix[m1][m] < target:
                        l2 = m + 1
                    else:
                        h2 = m - 1
                return False
        return False
