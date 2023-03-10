class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        
        t=0
        bfree=0
        lpushq,rpushq = [],[]
        lheap,rheap=[],[]
        
        for i in range(k):
            heapq.heappush(lheap , (-time[i][0]-time[i][2],-i) )
        
        while n>0 or rpushq or rheap:

            while lpushq and lpushq[0][0]<=t:
                _,i = heapq.heappop(lpushq)
                heapq.heappush( lheap ,  (-time[i][0]-time[i][2],-i))
            
            while rpushq and rpushq[0][0]<=t:
                _,i = heapq.heappop(rpushq)
                heapq.heappush( rheap ,  (-time[i][0]-time[i][2],-i))
                #print(rheap)
            
            
            if rheap:
                eff,i = heapq.heappop(rheap)
                i=-i
                bfree = t + time[i][2]
                heapq.heappush(lpushq, (bfree+time[i][3],i))
                print(f'{i} starts crossing from R->L at {t}')
            elif n>0 and lheap:
                eff,i = heapq.heappop(lheap)
                eff,i=-eff,-i
                bfree = t + time[i][0]
                heapq.heappush(rpushq , (bfree+time[i][1],i))
                print(f'{i} starts crossing from L->R at {t}')
                n-=1
            t=max(bfree,t+1)

        return bfree