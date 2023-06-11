class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        
        n=len(nums)
        cost=nums.copy()
        ans = sum(cost)
        
        for i in range(1,n):
            c = i*x
            
            for j in range(n):
                cost[j] = min(cost[j] , nums[(j+i)%n])
                c+=cost[j]
            
            ans = min(ans,c)
        
        return ans