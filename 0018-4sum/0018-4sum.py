class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n=len(nums)
        mp={}
        for i in range(n):
            mp[target-nums[i]]=i
        ans=[]
        added=set()
        for i in range(n-3):
            for j in range(i+1,n-2):
                for k in range(j+1,n-1):
                    tsum=nums[i]+nums[j]+nums[k]
                    idx=mp.get(tsum,0)
                    if idx>k:
                        ans.append([nums[i],nums[j],nums[k],nums[idx]])
                        if tuple(sorted(ans[-1])) in added:
                            ans.pop()
                        else:
                            added.add( tuple(sorted(ans[-1])) )
                        
        return ans