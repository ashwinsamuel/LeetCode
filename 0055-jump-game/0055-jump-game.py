class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n=len(nums)
        if n==1:
            return True
        
        
        for i in range(n-1):
            if nums[i]==0:
                j=i-1
                while j>=0 and nums[j]<i-j+1: j-=1

                if j<0:
                    return False
        
        return True