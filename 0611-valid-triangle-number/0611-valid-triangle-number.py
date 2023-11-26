class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        ans=0
        for i in range(n-1):
            for j in range(i+1,n):
                tsum = nums[i]+nums[j]
                idx = bisect_left(nums , tsum)
                ans+= max( idx-1-j , 0)
        return ans
                