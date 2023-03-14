# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(head,path,ans):
            if not head.left and not head.right:
                ans.append(path*10+head.val)
                return
            
            path = path*10+head.val
            if head.left: dfs(head.left, path, ans)
            if head.right: dfs(head.right, path, ans)
            path=path//10
            
            return
        
        ans=[]
        path=0
        dfs(root,path,ans)
        return sum(ans)
                