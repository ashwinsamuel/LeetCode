class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        tsum = sum(weights)
        n=len(weights)
        min_ans = tsum//n +1 if tsum%n else tsum//n
        
        def is_possible(weights,days,tans):
            i=0
            n=len(weights)
            while i< n and days>0:
                tsum=0
                while i<n and tsum<=tans:
                    tsum+=weights[i]
                    i+=1
                
                if tsum>tans:
                    i-=1
                    tsum-=weights[i]
                days-=1
                if days == 0 and i<n: return False
            
            return True
        
        
        
        l,r=min_ans,int(25e6+1)
        while True:
            tans = (l+r)//2

            ok = is_possible(weights,days,tans)
            if ok: r=tans
            else: l=tans
                
            if r==l+1: return r
            
            