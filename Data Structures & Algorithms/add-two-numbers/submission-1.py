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
        while ptr1 and ptr2:
            cnt = ptr1.val + ptr2.val + x2
            x1 = cnt%10
            x2 = cnt//10
            px.next = ListNode(x1)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            px = px.next
        
        while ptr1:
            cnt = ptr1.val + x2
            x1 = cnt % 10
            x2 = cnt // 10
            px.next = ListNode(x1)
            px = px.next
            ptr1 = ptr1.next
        while ptr2:
            cnt = ptr2.val + x2
            x1 = cnt % 10
            x2 = cnt // 10
            px.next = ListNode(x1)
            px = px.next
            ptr2 = ptr2.next
        if x2 != 0:
            px.next = ListNode(x2)
        return hd.next    