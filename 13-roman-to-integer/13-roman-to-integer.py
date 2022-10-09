class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        num = 0
        for i,letter in enumerate(s):
            if i+1 <= len(s)-1 and dic[letter] < dic[s[i+1]]:
                #subtraction
                num -= dic[letter]
            else:
                num += dic[letter]
        return num