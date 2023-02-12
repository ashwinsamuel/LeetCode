from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        que = deque([])
        depth=0
        que.append((root,depth))
        
        maxd = 0
        maxd_list = [root.val]
        while que:
            node,d = que.popleft()
            
            if node.left:
                newd = d+1
                que.append((node.left,newd))
                
                if newd > maxd:
                    maxd = newd
                    maxd_list = [node.left.val]
                elif newd == maxd:
                    maxd_list.append(node.left.val)
            
            if node.right:
                newd = d+1
                que.append((node.right,newd))
                
                if newd > maxd:
                    maxd = newd
                    maxd_list = [node.right.val]
                elif newd == maxd:
                    maxd_list.append(node.right.val)
        
        return sum(maxd_list)
            
            
        