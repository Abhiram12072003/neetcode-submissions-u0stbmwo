# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        curr = head
        for i in range(left-1):
            prev, curr = prev.next, curr.next
        px = None
        for i in range(right-left+1):
            tmp = curr.next
            curr.next = px
            px = curr
            curr = tmp
        prev.next.next = curr 
        prev.next = px
        
        return dummy.next 