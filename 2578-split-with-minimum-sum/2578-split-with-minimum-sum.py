class Solution:
    def splitNum(self, num: int) -> int:
        no = []
        while num>0:
            no.append(num%10)
            num//=10
        
        no.sort()
        n=len(no)
        tnum1,tnum2=0,0
        for i in range(0,n,2):
            tnum1 = tnum1*10 + no[i]
            if i+1<n: tnum2 = tnum2*10 + no[i+1]

        return tnum1+tnum2