"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return head
        if head.child==None:
            self.flatten(head.next)#n2 = self.flatten(head.next)
            #head.next = n2
            #if n2: n2.prev = head
            return head
        else:
            self.flatten(head.child)#c2 = self.flatten(head.child)
            c2 = head.child#head.child = None
            head.child=None
            before = curr = c2
            while curr:
                before=curr
                curr=curr.next
            
            self.flatten(head.next)#before.next = self.flatten(head.next)
            before.next = head.next
            if head.next: head.next.prev = before
            head.next = c2
            c2.prev = head
            
            return head
        
            
                
            
            
            
                
            