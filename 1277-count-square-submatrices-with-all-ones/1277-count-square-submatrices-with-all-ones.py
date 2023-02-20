class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        def calc(mat,i,j):
            ok=True
            ans=0
            d=1
            while i-d>=0 and j-d>=0:
                for k in range(d+1):
                    if not mat[i-k][j-d] or not mat[i-d][j-k]:
                        ok=False
                        break
                if ok: 
                    d+=1
                    ans+=1
                else: break
            return ans
        
        n=len(matrix)
        m=len(matrix[0])
        row = [0]*m
        dp = [row.copy() for i in range(n)]
        dp[0][0]=matrix[0][0]
        for i in range(1,n):
            dp[i][0]=dp[i-1][0]+matrix[i][0]
        for j in range(1,m):
            dp[0][j]=dp[0][j-1]+matrix[0][j]

        
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]:
                    dp[i][j]+=1
                    dp[i][j]+=calc(matrix,i,j)
                
                dp[i][j] += dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
                    
        return dp[n-1][m-1]
                    
                        
                    
                