# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        px = ListNode(0)
        dummy = px
        px.next = head
        for i in range(left-1):
            px = px.next
        print(px.val)
        prev, curr, tmp = None, px.next, px.next
        for i in range(right-left+1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # print(prev.val, curr.val)
        cnt = 0
        ptr = prev
        # while cnt < 8 and prev:
        #     print(prev.val, end = '')
        #     prev = prev.next
        #     cnt += 1
        # print()
        # prev.next = px
        px.next.next = curr
        px.next = prev
        return dummy.next