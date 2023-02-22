class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        arr = [lo+i for i in range(hi-lo+1)]
        if lo==1: k-=1
            
        while k>0:
            for idx,num in enumerate(arr):
                if num==1:
                    continue
                elif num%2:
                    arr[idx] = num*3+1
                else:
                    arr[idx] = num/2
                    if num==2:
                        k-=1
                        if k==0: return lo+idx
        return 1