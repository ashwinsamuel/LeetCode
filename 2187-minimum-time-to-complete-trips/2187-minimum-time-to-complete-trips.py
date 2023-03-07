class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time = sorted(time)
        n=len(time)
        
        #min k s.t. k//time[0] + k//time[1] + ...k//time[id] >= totalTrip        
        l = 0
        #r = time[-1]*(totalTrips//n+1) if totalTrips>=n else time[totalTrips-1]
        r=10**14
        while l<r:
            m=(l+r)//2
            k=bisect_right(time,m)
            trips=0
            for i in range(k):
                trips += m//time[i]       
                
            if trips>=totalTrips:
                r=m
            else:
                l=m+1
                
        return r
        