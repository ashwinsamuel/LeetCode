class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        end = (time//(n-1) )%2
        if end:
            return n - (time%(n-1))
        else:
            return 1+time%(n-1)