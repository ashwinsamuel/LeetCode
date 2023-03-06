# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        elif head.next==head: return True
        x1=head
        x2=head
        while x1 and x2 and x2.next:
            x1=x1.next
            x2=x2.next.next
            if x1==x2:
                return True
        return False