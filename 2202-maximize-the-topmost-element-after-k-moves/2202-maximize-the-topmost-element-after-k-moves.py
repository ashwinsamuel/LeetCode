class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if n==1: return -1 if k&1 else nums[0]
        if k==0: return nums[0]
        
        if k<n+1:
            ans = max(nums[:k-1],default=-1)
            return max(ans,nums[k] if k<n else -1)
        else:
            return max(nums)