from collections import deque
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n=len(nums)
        for i in range(1,n):
            nums[i]=nums[i]^nums[i-1]
        
        maxk = (1<<maximumBit) - 1
        ans = deque()
        for num in nums:
            k=num^maxk
            ans.appendleft(k)
        return ans