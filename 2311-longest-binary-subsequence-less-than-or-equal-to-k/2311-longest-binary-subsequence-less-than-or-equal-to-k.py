class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        if int(s,base=2) <=k:
            return len(s)
        
        num=int(s,2)
        n=len(s)
        r = -1
        while num%2:
            num = (num>>1)
            r-=1
        l=0
        while l<n and s[l]=='0':
            l+=1
        ll = (1<<(n-1-l) )
        
        num=int(s,2)
        ans=len(s)
        n=len(s)
        while num>k:
            if ll > (num>>1):
                #remove 1
                num-=ll
                l+=1
                while l<n and s[l]=='0':
                    l+=1
                ll=(1<<(n-1-l) ) if l!=n else -float('inf')
            else:
                #remove 0
                num-=(num>>1)
            ans-=1
        
            
        return ans