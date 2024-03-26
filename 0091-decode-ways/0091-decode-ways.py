class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def recurs(i):
            
            if i==n:
                return 1
            
            if i<n-1 and s[i] == "2" and s[i+1] in "0123456":
                return recurs(i+1)+recurs(i+2)
            elif i<n-1 and s[i]=="1":
                return recurs(i+1)+recurs(i+2)
            elif s[i] == "0":
                return 0
            else:
                return recurs(i+1)
            
        n=len(s)
        return recurs(0)