# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = l1, l2
        px = ListNode(1)
        hd = px
        x2 = 0
        while ptr1 or ptr2 or x2:
            v1 = ptr1.val if ptr1 else 0
            v2 = ptr2.val if ptr2 else 0
            val = v1 + v2 + x2
            x2 = val // 10
            val = val % 10
            px.next = ListNode(val)
            px = px.next
            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
        return hd.next    