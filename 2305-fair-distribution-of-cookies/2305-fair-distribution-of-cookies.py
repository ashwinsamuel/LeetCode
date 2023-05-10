class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        tsum = [0 for i in range(1<<len(cookies))]
        for i in range(1<<len(cookies)):
            for shift in range(len(cookies)):
                if (i>>shift)&1:
                    tsum[i]+=cookies[shift]
        
        
        dp = [[0 for msk in range(1<<len(cookies))] for i in range(k)]
        
        for msk in range(1<<len(cookies)):
            dp[0][msk]=tsum[msk]
            
        for i in range(1,k):
            for msk in range(1<<len(cookies)):              
                submsk = msk
                dp[i][msk]=float('inf')
                while submsk:
                    submsk = (submsk-1)&msk
                    xor = submsk^msk
                    dp[i][msk] = min(dp[i][msk] , max(dp[i-1][submsk],tsum[xor]))
        
        for i in range(k):
            print(dp[i])
        
        return dp[k-1][(1<<len(cookies))-1]
                    
    
        
        
        