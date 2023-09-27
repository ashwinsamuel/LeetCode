class Solution:
    def maximumSumOfHeights(self, A: List[int]) -> int:
        n = len(A)

        left = [0] * n
        stack = [-1]
        cur = 0
        for i in range(n):
            while len(stack) > 1 and A[stack[-1]] > A[i]:
                j = stack.pop()
                cur -= (j - stack[-1]) * A[j]
            cur += (i - stack[-1]) * A[i]
            stack.append(i)
            left[i] = cur

        stack = [n]
        res = cur = 0
        for i in range(n - 1, -1, -1):
            while len(stack) > 1 and A[stack[-1]] > A[i]:
                j = stack.pop()
                cur -= -(j - stack[-1]) * A[j]
            cur += -(i - stack[-1]) * A[i]
            stack.append(i)
            res = max(res, left[i] + cur - A[i])

        return res