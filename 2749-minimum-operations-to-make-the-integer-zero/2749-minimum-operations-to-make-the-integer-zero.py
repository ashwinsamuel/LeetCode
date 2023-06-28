class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        
        ans=1
        while True:
            tnum = num1 - ans*num2
            print(ans,tnum.bit_count(),tnum)
            if tnum<0:
                return -1
            elif (ans>=tnum.bit_count() and ans<=tnum):
                return ans
            else:
                ans+=1
        
        #print(ans,tnum,tnum.bit_count())
        return -1