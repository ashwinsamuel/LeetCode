class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        
        tmin=prices[0]
        tmax=prices[0]
        ans=0
        for i in range(1,n):
            if prices[i]<tmin:
                tmin=prices[i]
                tmax=0
            
            if prices[i]>tmax:
                tmax=prices[i]
                if tmax-tmin > ans:
                    ans=tmax-tmin
        
        return ans
            