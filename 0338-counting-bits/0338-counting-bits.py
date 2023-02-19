class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0: return [0]
        
        ans=[0,1]
        for p in range(1,20):
            for i in range(1<<p):
                if len(ans)==n+1:
                    return ans
                ans.append(ans[i]+1)
                    
            
        