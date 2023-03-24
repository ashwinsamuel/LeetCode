import heapq
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        ints = sorted(intervals,key=lambda x: x[0])
        
        grps=[]
        ans=0
        for l,r in ints:
            if len(grps)>0 and l>grps[0]:
                heapq.heappop(grps)
                heapq.heappush(grps,r)
            else:
                ans+=1
                heapq.heappush(grps,r)
        return ans