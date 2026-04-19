# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, node1, node2):
        dummy = ListNode(0)
        head = dummy
        while node1 and node2:
            if node1.val < node2.val:
                dummy.next = node1
                node1 = node1.next
            else:
                dummy.next = node2
                node2 = node2.next
            dummy = dummy.next
        if node1:
            dummy.next = node1
        if node2:
            dummy.next = node2
        return head.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while len(lists)>1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.merge(l1, l2))
            lists = mergedLists
        return lists[0]