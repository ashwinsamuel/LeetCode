# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        qu = deque()
        if root:
            qu.append(root)
        ans=[]
        while qu:
            ans.append([])
            
            tlen=len(qu)
            tlist=[]
            
            for i in range(tlen):
                tlist.append(qu.popleft())
            
            #queue is empty now
            
            for nd in tlist:
                ans[-1].append(nd.val)
                
                if nd.left:
                    qu.append(nd.left)
                if nd.right:
                    qu.append(nd.right)
        
        return ans
        
        
                
            
        
        