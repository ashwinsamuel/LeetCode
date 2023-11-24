class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        
        def ham_dist(i,j):
            m=len(words[i])
            ans=0
            for k in range(m):
                if words[i][k] != words[j][k]:
                    ans+=1
            return ans
        
        n=len(groups)
        dp = [[] for i in range(n)]
        for i in range(n):
            tmax = 1
            tmaxi = i
            for j in range(i):
                if len(dp[j])+1>tmax and groups[i] != groups[j] and len(words[i])==len(words[j]) and ham_dist(i,j)==1:
                    tmax=len(dp[j])+1
                    tmaxi=j
                    
            dp[i] = dp[tmaxi].copy()
            dp[i].append(i)
        
        ans=0
        for i in range(n):
            if len(dp[i])>ans:
                ans=len(dp[i])
                ansi = i
            print(dp[i])
        print(ansi)
        result=[]
        for idx in dp[ansi]:
            result.append(words[idx])
        return result
    
        
                    