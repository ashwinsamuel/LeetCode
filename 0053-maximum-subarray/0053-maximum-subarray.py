class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_ending_here = n * [nums[0]]
        for i in range(1, n):
            max_ending_here[i] = max(max_ending_here[i-1] + nums[i], nums[i])
        return max(max_ending_here)