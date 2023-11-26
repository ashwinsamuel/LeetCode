class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        ans=0
        
        for i in range(n-2):
            j = i+1
            tsum = nums[i]+nums[j]
            idx = bisect_left(nums , tsum)
            ans+= max( idx-1-j , 0)
            #print(i, j, ans)
            
            while j<n-1:
                j+=1
                tsum = nums[i]+nums[j]
                while idx<n and nums[idx]<tsum: idx+=1
                ans+= max( idx-1-j , 0)
                
                #print(i, j, ans)
            
        return ans
        
        
        '''
        for i in range(n-1):
            for j in range(i+1,n):
                tsum = nums[i]+nums[j]
                idx = bisect_left(nums , tsum)
                ans+= max( idx-1-j , 0)
        return ans
        '''