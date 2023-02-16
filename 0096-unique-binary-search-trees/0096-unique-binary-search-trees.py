class Solution:
    def numTrees(self, n: int) -> int:
        dp=[]
        dp.append(1)
        dp.append(1)
        dp.append(2)
        
        for i in range(3,n+1):
            tsum = 0
            for j in range(i):
                tsum+= dp[j]*dp[i-j-1]
            dp.append(tsum)
        
        return dp[n]