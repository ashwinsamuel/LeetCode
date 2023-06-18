class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        #14! * 14 or (14 nested loops)
        n=len(nums)
        MOD=(10**9)+7
        @cache
        def dfs(nd,msk):
            if msk == (1<<n)-1:
                return 1    
            tans = 0
            for i in range(n):
                if not msk&(1<<i) and (nums[i]%nd==0 or nd%nums[i]==0):
                    tans = (tans + dfs(nums[i], msk|(1<<i)))%MOD
            return tans

        return dfs(1,0)
            
        
        
        
            
        