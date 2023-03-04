from collections import deque
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n=len(nums)
        for i in range(1,n):
            nums[i]=nums[i]^nums[i-1]
        
        ans = deque()
        for num in nums:
            k=0
            for shift in range(maximumBit):
                if num & 1<<shift == 0:
                    k = k | 1<<shift
            ans.appendleft(k)
        return ans