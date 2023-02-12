class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n=len(nums)
        ans = 0
        
        for lo in nums:
            #lower <= lo + up <= upper
            #lower - lo <= up <= upper - lo
            
            l = bisect.bisect_left(nums, lower-lo)
            r = bisect.bisect_right(nums, upper-lo)
            
            ans += r-l
            if lower-lo<=lo<=upper-lo:
                ans-=1
        
        return ans//2