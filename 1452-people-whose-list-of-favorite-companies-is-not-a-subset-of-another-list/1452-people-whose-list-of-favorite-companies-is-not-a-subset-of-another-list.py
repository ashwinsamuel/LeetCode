class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n=len(favoriteCompanies)
        sz = [(len(favoriteCompanies[i]),i) for i in range(n)]
        sz.sort(reverse=True)
        
        ans = [True]*n
        mp = {}
        for m,i in sz:
            bitwise = (1<<n) - 1
            for comp in favoriteCompanies[i]:
                bitwise &= mp.get(comp,0)
                mp[comp] = mp.get(comp,0) | (1<<i)
            
            if bitwise!=0:
                ans[i]=False
        
        result=[]
        for i in range(n):
            if ans[i]: result.append(i)
        return result