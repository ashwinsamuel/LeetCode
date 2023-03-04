class Solution:
    def twoEggDrop(self, n: int) -> int:
        
        dp=[0,1]
        
        for i in range(2,n+1):
            dp.append(i)
            for x in range(1,i):
                dp[i] = min( dp[i] , max(x,dp[i-x]+1) )
        return dp[n]