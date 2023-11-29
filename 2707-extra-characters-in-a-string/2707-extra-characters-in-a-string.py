class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        n=len(dictionary)
        @cache
        def dp(i):
            
            if i==len(s):
                return 0
            
            tans=len(s)
            for j in range(n):
                w = dictionary[j]
                if s[i:i+len(w)] == w:
                    tans = min(dp(i+len(w)) , tans)
            
            tans = min(1+dp(i+1) , tans)

            return tans
        
        #print(s[:50] == "leetscodeoo")
        
        return dp(0)
                
            
            