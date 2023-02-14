class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
                        
        def sentences(s,i,words,dp):
            if i==len(s):
                return []

            ans=[]
            for w in words:
                if w == s[i:i+len(w)]:
                    if i+len(w) in dp:
                        tlist = dp[i+len(w)].copy()
                    else:
                        tlist = sentences(s,i+len(w),words,dp).copy()
                        
                    if tlist:
                        for k in range(len(tlist)):
                            tlist[k] = s[i:i+len(w)] + " " + tlist[k]
                        ans += tlist
                    elif i+len(w) == len(s):
                        ans += [s[i:i+len(w)]]
                        

            dp[i]=ans
            return ans
        
        dp={}
        ans = sentences(s,0,wordDict,dp)
        if 4 in dp:
            print(dp[4])
        return ans
        
        
            