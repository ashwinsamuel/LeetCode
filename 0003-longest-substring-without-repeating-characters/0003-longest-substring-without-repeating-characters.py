class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        max_len = 0
        length = 0
        start = 0
        for i,letter in enumerate(s):
            if letter in dic and dic[letter] >= start:
                start = dic[letter] + 1
                length = i - dic[letter]
                dic[letter] = i

            else:
                dic[letter] = i
                length+=1
                if length > max_len:
                    max_len = length     

        return max_len