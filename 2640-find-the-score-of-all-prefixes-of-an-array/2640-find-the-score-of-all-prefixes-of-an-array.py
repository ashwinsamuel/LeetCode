class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        max_num = float('-inf')

        for i in range(n):
            max_num = max(max_num, nums[i])
            ans[i] = nums[i] + max_num

        tsum=ans[0]
        for i in range(1,n):
            ans[i]+=tsum
            tsum=ans[i]
        return ans