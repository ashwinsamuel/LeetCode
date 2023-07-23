class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        prevx,prevy=points[0]
        ans=0
        for x,y in points[1:]:
            ans+=max( abs(prevx-x) , abs(prevy-y) )
            prevx,prevy=x,y
        return ans