class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        max_ending_here0 = n * [arr[0]]  # no deletion
        max_ending_here1 = n * [arr[0]]  # at most 1 deletion
        for i in range(1, n):
            max_ending_here0[i] = max(max_ending_here0[i-1] + arr[i], arr[i])
            max_ending_here1[i] = max(max_ending_here1[i-1] + arr[i], arr[i])
            if i >= 2:
                max_ending_here1[i] = max(max_ending_here1[i], max_ending_here0[i-2] + arr[i])
        return max(max_ending_here1)