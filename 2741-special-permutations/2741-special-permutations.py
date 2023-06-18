class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n, MOD = len(nums), 10**9 + 7
        @cache
        def dfs(index, prev, mask):
            if mask == (1 << n) - 1: return 1
            count = 0
            for i in range(n):
                if not (mask & (1 << i)) and (nums[i] % prev == 0 or prev % nums[i] == 0):
                    count += dfs(index + 1, nums[i], mask | (1 << i))
            return count % MOD
        return dfs(0, 1, 0)
        
        
        
            
        