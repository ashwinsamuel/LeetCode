class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n=len(nums)
        presum=[0]
        for i in range(n):
            if nums[i]%modulo==k:
                presum.append((presum[-1]+1)%modulo)
            else:
                presum.append(presum[-1])
        
        print(presum)
        
        i,n=0,len(presum)
        cnt={}
        while i<n:
            if presum[i]==k:
                break
            else:
                cnt[presum[i]]=cnt.get(presum[i],0)+1
            i+=1
        
        ans=0
        while i<n:
            key = (presum[i]-k+modulo)%modulo
            ans+=cnt.get(key,0)
            
            cnt[presum[i]]=cnt.get(presum[i],0)+1
            i+=1
        return ans
        
        
            
            