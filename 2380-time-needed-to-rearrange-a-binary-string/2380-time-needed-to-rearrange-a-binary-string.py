class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        #smartly or pure coding
        #cant change chr of str
        
        ans=0
        n=len(s)
        st = [s[i] for i in range(n)]
        while True:
            ok=False
            notok=False
            for j in range(n-1):
                if st[j]=='0' and st[j+1]=='1' and notok==False:
                    ok=True
                    st[j] , st[j+1]='1','0'
                    notok =True
                elif notok:
                    notok=False
            if not ok:
                return ans
            ans+=1
        return ans
                
                    