class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        
        ans=0
        for i in range(n):
            for j in range(m):
                miss=0
                p=i
                for k in range(j,m):
                    if s[p] == t[k]:
                        if miss==1: ans+=1
                    else:
                        if miss==0:
                            miss+=1
                            ans+=1
                        else:
                            break
                    p+=1
                    if p==n: break
        return ans
            
                    
                