# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head=head.next
        curr=head
        
        while curr:
            temp=curr
            tsum=0
            while temp.val !=0:
                tsum+=temp.val
                temp=temp.next
            curr.val=tsum
            curr.next = temp.next
            curr=temp.next
            
        return head
            