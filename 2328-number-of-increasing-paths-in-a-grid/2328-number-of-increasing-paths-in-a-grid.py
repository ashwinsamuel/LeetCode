class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j,dp,n,m,grid):
            if i*m+j in dp:
                return dp[i*m+j]
    
            cnt=0
            for nei,nej in [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]:
                if 0<=nei<n and 0<=nej<m and grid[nei][nej] > grid[i][j]:
                    cnt+=dfs(nei,nej,dp,n,m,grid)
            dp[i*m+j]=cnt+1
            return cnt+1 
        
        mod=10**9+7
        n,m=len(grid),len(grid[0])
        dp = {}
        for i in range(n):
            for j in range(m):
                if i*m+j not in dp:
                    dfs(i,j,dp,n,m,grid)
        ans=0
        for k,v in dp.items(): ans = (ans+v)%mod
        return ans