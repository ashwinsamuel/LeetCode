class Solution:
    def longestPalindrome(self, s: str) -> str:
        dic = {}
        even_center = []
        odd_center = []
        for i,letter in enumerate(s):
            if letter in dic and i-dic[letter] == 2:
                odd_center.append(i)
            elif letter in dic and i-dic[letter] == 1:
                if dic[letter] > 0 and letter == s[dic[letter] - 1]:
                    odd_center.append(i)                
                even_center.append(i)
            dic[letter] = i
        
        substr = s[0]
        length = 1
        max_len = 1
        #odd center counting
        for i in range(len(odd_center)):
            gap=2
            last = odd_center[i]
            while(last >= gap and s[last] == s[last-gap]):
                gap+=2
                last+=1
                if last >= len(s):
                    break
            length = gap-1
            if length > max_len:
                max_len=length
                substr = s[last-gap+1:last]
            
        #even center counting
        for i in range(len(even_center)):
            gap=1
            last = even_center[i]
            while(last >= gap and s[last] == s[last-gap]):
                gap+=2
                last+=1
                if last >=len(s):
                    break
            length = gap-1
            if(length > max_len):
                max_len=length
                substr = s[last-gap+1:last]
        
        return substr