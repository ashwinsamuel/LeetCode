# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def maxpath(node):
            
            nonlocal ans
            
            if not node:
                return 0
            
            l = maxpath(node.left)
            r = maxpath(node.right)
            
            #print(ans , node.val + l + r)
            ans = max(ans , node.val + max(l,0) + max(r,0))
            return max(l,r,0)+node.val
            
        
        ans=-float('inf')
        maxpath(root)
        
        return ans