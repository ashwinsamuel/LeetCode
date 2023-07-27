class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        '''
        dp[n,k] = min( max(dp[n-2,k-1],nums[n]) , dp[n-1,k] )
        O(n*k)       
        '''
        '''
        @cache
        def dp(i,p):
            
            if i==0:
                if p>1:
                    return float('inf') , float('inf')
                elif p==1:
                    return float('inf') , nums[0]
                else:
                    return 0 , 0

            tans0,tans1 = dp(i-1,p)
            t1ans0 , t1ans1 = dp(i-1,p-1)
            return min( tans0 , tans1 ) , max(t1ans0,nums[i])
        
        n=len(nums)
        return min(dp(n-1,k))
        '''
        
        def check(ans):
            
            prev = [0,1] if nums[0]<=ans else [0,0]
            for i in range(1,n):
                if nums[i]<=ans:
                    chg = 1
                else:
                    chg=0
                curr = [max(prev) , prev[0]+chg]
                
                if max(curr)>=k:
                    return True
                prev = curr
            
            return False
            
        n=len(nums)
        l = min(nums)
        r = max(nums)
        while l<r:
            mid = (l+r)//2
            ok = check(mid)
            if ok:
                r=mid
            else:
                l=mid+1
        
        return r