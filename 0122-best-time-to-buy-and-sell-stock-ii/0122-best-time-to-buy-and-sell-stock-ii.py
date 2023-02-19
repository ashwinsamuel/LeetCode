class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n==1: return 0
        diff = [prices[i+1]-prices[i] for i in range(n-1)]
        
        ans=0
        for d in diff:
            if d>0: ans+=d
        return ans