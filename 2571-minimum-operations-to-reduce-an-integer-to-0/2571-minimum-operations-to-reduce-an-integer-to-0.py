class Solution:
    def minOperations(self, n: int) -> int:
        
        powers = [1<<i for i in range(20)]
        
        idx = bisect.bisect_right(powers,n)
        if n==powers[idx-1]: return 1
        
        lans , rans=1,1
        l,r = powers[idx-1] , powers[idx]
        while True:
            mid = (l + r)//2
            if n == mid: return min(lans,rans) + 1
            elif n<mid:
                rans=min(lans,rans)+1
                r=mid
            else:
                lans=min(lans,rans)+1
                l=mid
                
                
                