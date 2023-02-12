class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        div = n-2
        num = ""
        while n>0:
            num = str(n%div) + num
            n /= div
        
        l=0
        r=len(num)-1
        while l<r:
            if num[l] != num[r]:
                return False
            l+=1
            r-=1
        
        return True