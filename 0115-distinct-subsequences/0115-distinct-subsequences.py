class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        
        word_ending = {j:0 for j in range(m)}
        for i in range(n):
            updates=[]
            for j in range(m):
                if s[i]==t[j]:
                    if j==0:
                        updates.append((j,1))
                    else:
                        updates.append((j,word_ending[j-1]))
            
            for idx,upd in updates:
                word_ending[idx] += upd
    
        return word_ending[m-1]
                        