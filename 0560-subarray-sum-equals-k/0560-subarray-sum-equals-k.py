class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        mp = {0:1}
        tsum=0
        ans=0
        for i in range(n):
            tsum+=nums[i]
            ans+= mp.get(tsum-k , 0)
            mp[tsum] = mp.get(tsum,0)+1
        return ans
            