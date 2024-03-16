class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n=len(nums)
        
        lmax = nums[0]
        ans = 1
        tmax = -float('inf')
        for i in range(1,n):
            if lmax <= nums[i]:
                tmax = max(tmax,nums[i])
            else:
                ans = i+1
                lmax = max(tmax,lmax)
                tmax = -float('inf')
        return ans
            
            
            