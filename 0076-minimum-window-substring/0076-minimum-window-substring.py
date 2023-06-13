class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = Counter(t)
        curr = {}
        cnt = len(dic.items())
        
        l,r=0,0
        n=len(s)
        while r<n:
            ch = s[r]
            curr[ch] = curr.get(ch , 0)+1
            if curr[ch] == dic.get(ch,0):
                cnt-=1
                if cnt==0:
                    break
            r+=1
        
        print(f'first {l},{r}')
        
        if cnt>0:
            return ""
        else:
            ans = s[:r+1]
            tmin = r+1
            while True:
                ch = s[l]
                l+=1
                curr[ch] -=1
                if ch in dic and curr[ch]<dic[ch]:
                    #keep going till curr[ch]+=1
                    r+=1
                    while r<n:
                        ch2 = s[r]
                        curr[ch2] = curr.get(ch2,0)+1
                        if ch2 == ch:
                            break
                        r+=1
                    if r==n:
                        break
                print(l,r)
                if r-l+1<tmin:
                    ans = s[l:r+1] #could be optimized
                    tmin = r-l+1
        
        return ans