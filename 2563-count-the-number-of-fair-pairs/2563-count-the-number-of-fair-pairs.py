class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums = sorted(nums)
        n = len(nums)
        ans = 0
        h,l=n-1,n-1
        for i in range(n):
            while h>= 0 and nums[i]+nums[h] > upper: h-=1
            while l>= 0 and nums[i]+nums[l] >= lower: l-=1
            
            ans += h-l
            if l<i<=h:
                ans-=1
            
        return ans//2