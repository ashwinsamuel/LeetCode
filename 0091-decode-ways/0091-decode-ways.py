class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [1]
        if s[0] == "0":
            dp.append(0)
        else:
            dp.append(1)
            
        for i in range(1,len(s)):
            if s[i] == "0":
                if s[i-1] in "12":
                    dp.append(dp[i-1])
                else:
                    dp.append(0)
            else:
                if s[i-1] == "1" or (s[i-1] == "2" and s[i] in "123456"):
                    dp.append(dp[i-1] + dp[i])
                else:
                    dp.append(dp[i])

        return dp[len(s)]