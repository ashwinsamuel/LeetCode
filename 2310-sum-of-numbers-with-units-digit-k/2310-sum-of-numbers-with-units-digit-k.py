class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num==0: return 0
        if k==0: return 1 if num%10==0 else -1
        
        poss=k
        visited=set()
        while (poss%10) not in visited:
            if num%10 == poss%10:
                return poss//k if poss<=num else -1
            visited.add(poss%10)
            poss+=k
        
        return -1