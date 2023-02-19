class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        vow = ['a','e','i','o','u']
        
        #f(n,a) = for c in "aeiou" f(n-1,c) 
                #+ [for c in "eiou" f(n-1,c)] 
                #+ [f(n-1,c) in "iou"]
                
        dp=[{} for i in range(n+1)]
        for c in "aeiou":
            dp[1][c] = 1
        
        for i in range(2,n+1):
            for ch in "aeiou":
                dp[i][ch] = 0
                idx = vow.index(ch)
                for c in vow[idx:]:
                    dp[i][ch] += dp[i-1][c]
        
        return sum(dp[n][c] for c in "aeiou")