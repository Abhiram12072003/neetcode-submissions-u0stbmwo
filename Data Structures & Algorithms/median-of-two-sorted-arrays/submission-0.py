class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        l1, h1 = 0, len(nums1) - 1
        while True:
            m1 = (l1+h1)//2
            m2 = half - m1 - 2
            aleft = nums1[m1] if m1 >= 0 else float("-infinity")
            aright = nums1[m1+1] if (m1+1) < len(nums1) else float("infinity")
            bleft = nums2[m2] if m2>=0 else float("-infinity")
            bright = nums2[m2+1] if (m2+1) < len(nums2) else float("infinity")
            if aleft<=bright and bleft<=aright:
                if total % 2:
                    return min(aright, bright)
                # else:
                return (max(aleft, bleft) + min(aright, bright))/2
            elif aleft > bright:
                h1 = m1 - 1
            else:
                l1 = m1 + 1
        return -1
