class Solution:
    def maxDepth(self, s: str) -> int:
        
        d=0
        ans=0
        for ch in s:
            if ch =='(':
                d+=1
                ans=max(ans,d)
            elif ch ==')':
                d-=1
        return ans
                