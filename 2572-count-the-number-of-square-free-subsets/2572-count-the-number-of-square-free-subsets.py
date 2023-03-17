class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        def prime_fact(num):
            n=(num**0.5)//1
            prime = [2,3,5,7,11,13,17,19,23,29]
            ans = 0
            for p in prime:
                if num%p==0:
                    ans = ans | (1<<prime.index(p))
                    num = num//p
                    if num%p==0:
                        return 1024
            return ans                    
                    
        
        n=len(nums)
        MaxN=1e9+7
        #Edge case about 1 and stuff
        dp = [[0 for i in range(n+1)] for j in range(1024)]
        for i in range(1,n+1):
            factors = prime_fact(nums[i-1])
            if factors<1024: 
                dp[factors][i] +=1
                for k in range(1024):
                    dp[k][i]= (dp[k][i] + dp[k][i-1]) % MaxN
                    if k & factors == 0:
                        dp[k|factors][i] = (dp[k|factors][i] + dp[k][i-1])%MaxN
            else:
                for k in range(1024):
                    dp[k][i]= (dp[k][i] + dp[k][i-1]) % MaxN
        
        return int(sum(dp[k][n] for k in range(1024)) % MaxN)