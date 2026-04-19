# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1, ptr2 = head, head
        itr = 0
        dummy = ListNode(0, head)
        ptr1 = dummy
        while itr<n:
            ptr2 = ptr2.next
            itr += 1
        while ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr1.next = ptr1.next.next
        return dummy.next