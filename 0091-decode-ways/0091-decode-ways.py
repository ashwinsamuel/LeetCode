class Solution:
    def numDecodings(self, s: str) -> int:
        only_units = set("0")
        solo_units1 = set(["3","4","5","6"])
        solo_units2 = set(["7","8","9"])
        tens_solo_units = set(["1","2"])

        dp = [1]
        if s[0] in only_units:
            dp.append(0)
        else:
            dp.append(1)

            
        for i in range(1,len(s)):
            if s[i] in only_units:
                if s[i-1] in tens_solo_units:
                    if s[i-1] == "2" and s[i] in solo_units2: 
                        dp.append(0)
                    else:
                        dp.append(dp[i-1])
                else:
                    dp.append(0)
            else:
                if s[i-1] in tens_solo_units:
                    if s[i-1] == "2" and s[i] in solo_units2:
                        dp.append(dp[i])
                    else:
                        dp.append(dp[i-1] + dp[i])
                else:
                    dp.append(dp[i])

        return dp[len(s)]