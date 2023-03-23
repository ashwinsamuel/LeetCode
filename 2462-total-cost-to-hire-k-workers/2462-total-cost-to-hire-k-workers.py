import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n=len(costs)
        l,r=candidates,n-candidates-1
        if l<=r:
            lheap = costs[:candidates]
            rheap = costs[-candidates:]
            heapq.heapify(lheap)
            heapq.heapify(rheap)
        else:
            lheap=costs
            rheap=[]
        
        ans=0
        sesh=0
        while l<=r and sesh<k:
            if rheap[0] < lheap[0]:
                tans = heapq.heappop(rheap)
                print(tans)
                ans+=tans
                heapq.heappush(rheap,costs[r])
                r-=1
            else:
                tans = heapq.heappop(lheap)
                print(tans)
                ans+=tans
                heapq.heappush(lheap,costs[l])
                l+=1
            sesh+=1
        
        if sesh==k: return ans
        else:
            lheap.extend(rheap)
            heapq.heapify(lheap)
            while sesh<k:
                ans+=heapq.heappop(lheap)
                sesh+=1
            return ans
        
        
        
        
        