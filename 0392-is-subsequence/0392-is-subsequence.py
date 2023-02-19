class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m=len(s)
        if m==0: return True
        i=0
        for c in t:
            if c==s[i]:
                i+=1
                if i==m: return True
        
        return False