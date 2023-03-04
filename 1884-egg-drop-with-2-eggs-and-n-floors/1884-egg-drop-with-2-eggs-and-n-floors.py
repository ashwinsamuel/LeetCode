class Solution:
    def twoEggDrop(self, n: int) -> int:
        
        dp=[0,1]
        
        for i in range(2,n+1):
            dp.append(i)
            for x in range(1,i):
                temp = max(x,dp[i-x]+1)
                if temp>dp[i]:
                    break
                else:
                    dp[i] = temp
        return dp[n]