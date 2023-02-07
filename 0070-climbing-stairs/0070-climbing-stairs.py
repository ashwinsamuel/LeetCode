class Solution:
    def climbStairs(self, n: int) -> int:
        if n<2:
            return 1
        else:
            a = []
            a.append(1)
            a.append(1)
            for i in range(2,n+1):
                a.append(a[i-2] + a[i-1])
            
            return a[n]