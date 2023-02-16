class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #any letter comes
        #1. words ending till letter now
        
        n=len(s)
        m=len(t)
        
        word_ending = {}
        for i in range(n):
            updates=[]
            for j in range(m):
                if s[i]==t[j]:
                    if j==0:
                        updates.append((j,1))
                    
                    if j-1 in word_ending:
                        updates.append((j,word_ending[j-1]))
            
            for idx,upd in updates:
                if idx not in word_ending:
                    word_ending[idx] = upd
                else:
                    word_ending[idx] += upd
    
        return word_ending[m-1] if m-1 in word_ending else 0
                        