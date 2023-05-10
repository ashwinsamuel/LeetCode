class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        
        tx,ty=target
        sx,sy = start
        pq=[(0,sx,sy)]
        dist = {}
        
        while pq:
            d,x,y = heapq.heappop(pq)
            
            for x1,y1,x2,y2,cost in specialRoads:
                if d+abs(x-x1)+abs(y-y1)+cost < dist.get((x2,y2),float('inf')):
                    dist[(x2,y2)] = d+abs(x-x1)+abs(y-y1)+cost
                    heapq.heappush(pq, (dist[(x2,y2)], x2,y2) )
        
        ans=abs(sx-tx)+abs(sy-ty)
        for x1,y1,x2,y2,cost in specialRoads:
            ans = min( ans , dist[(x2,y2)] + abs(x2-tx) + abs(y2-ty))
        
        return ans
        
        
                    
                