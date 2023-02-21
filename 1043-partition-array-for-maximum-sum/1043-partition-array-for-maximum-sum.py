class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[0,arr[0]]
        
        for i in range(1,n):
            msum=0
            for j in range(min(k,i+1)):
                tsum = max(arr[i-j:i+1])*(j+1) + dp[i-j]
                if tsum > msum:
                    msum = tsum
            dp.append(msum)
        
        return dp[n]