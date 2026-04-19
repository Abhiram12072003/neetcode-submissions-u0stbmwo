# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        px1 = head
        cnt1 = 1
        while px1:
            if cnt1 == left:
                left = px1
            if cnt1 == right:
                right = px1
                break
            cnt1 += 1
            px1 = px1.next
        ptr1, ptr2 = None, None
        if head != left:
            ptr1 = head
            while ptr1.next != left:
                ptr1 = ptr1.next
            
            ptr1.next = None
        
        if right.next:
            ptr2 = right.next
            right.next = None
        pt1, pt2, pt3 = None, left, left
        # print(pt2.val, pt3.val)
        while pt2 is not None:
            pt3 = pt2.next
            pt2.next = pt1
            pt1 = pt2
            pt2 = pt3
        if ptr2:
            left.next = ptr2
        if not ptr1:
            return pt1
        else:
            ptr1.next = pt1

        return head