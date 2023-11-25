class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        '''
        j -> 0 to 2n
        dp[i][j] = max( (ith object takes A) + dp[i-1][j-1] , dp[i-1][j] + (ith object takes B) )
        '''
        
        n2 = len(costs)
        dp = [[costs[0][1] , costs[0][0]]]
        for i in range(1,n2):
            
            ll = []
            for j in range(i+2):
                #j A's till now
                tans=float('inf')
                if j>0: tans = min( dp[i-1][j-1]+costs[i][0] , tans )
                if j<=i: tans = min(dp[i-1][j]+costs[i][1] , tans)
                ll.append( tans )
            
            #print(i,ll)
            dp.append(ll)
        
        return dp[n2-1][n2//2]
                