class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        pos = {a: i + 1 for i,a in enumerate(nums)}
        res = n = len(nums)
        i = 0
        for k,a in enumerate(sorted(nums)):
            if pos[a] < i:
                res += n - k
            i = pos[a]
        return res