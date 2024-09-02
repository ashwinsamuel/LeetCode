class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        cnt = [1,9,81]
        prev=8
        for i in range(3,n+1):
            cnt.append(cnt[-1]*prev)
            prev-=1
            
        return sum(cnt[:n+1])