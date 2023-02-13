class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        #dp[max_path] in the parent dfs call
        
        #make graph
        n=len(arr)
        adj = [[] for i in range(n)]
        for i in range(n):
            right=True
            left=True
            jump=1
            while (right or left) and jump<=d :
                if right:
                    if i+jump<n and arr[i+jump]<arr[i]:
                        adj[i].append(i+jump)
                    else:
                        right=False
                
                if left:
                    if i-jump>=0 and arr[i-jump]<arr[i]:
                        adj[i].append(i-jump)
                    else:
                        left=False
                
                jump+=1
                    
        #dfs
        def dfs(i,adj,max_path):

            if not adj[i]:
                max_path[i]=1
                return 1
            
            max_depth=0
            for neigh in adj[i]:
                if neigh not in max_path:
                    depth=dfs(neigh,adj,max_path)
                else:
                    depth = max_path[neigh]
                
                if depth>max_depth:
                    max_depth = depth

            max_path[i]=max_depth+1
            return max_path[i]
            
        
        max_path={}
        Mroot_path=0
        Mroot=0
        path=set()
        for i in range(n):
            if i not in max_path:
                max_path[i] = dfs(i,adj,max_path)
                
                if max_path[i] > Mroot_path:
                    Mroot=i
                    Mroot_path=max_path[i]
        
        return Mroot_path
                
        
        