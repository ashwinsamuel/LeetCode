class Solution:
    def better(self, x: int, y: int) -> int:
        return y if y >= 0 and (x < 0 or x > y) else x

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        limit = n << 1
        m = limit | 1
        dp = [[-1] * m for _ in range(2)]
        dp[0][n] = 0
        last = 0
        for i in range(n):
            now = last ^ 1
            dp[now] = [-1] * m
            for j in range(limit + 1):
                if dp[last][j] >= 0:
                    dp[now][min(limit, j + time[i])] = self.better(dp[now][min(limit, j + time[i])], dp[last][j] + cost[i])
                    if j:
                        dp[now][j - 1] = self.better(dp[now][j - 1], dp[last][j])
            last ^= 1
        r = -1
        for i in range(n, limit + 1):
            r = self.better(r, dp[last][i])
        return r