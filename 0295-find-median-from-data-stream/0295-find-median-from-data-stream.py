import heapq
class MedianFinder:

    def __init__(self):
        self.minh = []
        self.maxh = []

    def addNum(self, num: int) -> None:
        
        
        
        if len(self.maxh)==0 or num < -self.maxh[0]:
            heapq.heappush(self.maxh , -num)
            
            if len(self.maxh) - len(self.minh) >=2:
                heapq.heappush(self.minh , -heapq.heappop(self.maxh))
            
        elif len(self.minh)==0 or num > self.minh[0]:
            heapq.heappush(self.minh , num)
            
            if len(self.minh) - len(self.maxh) >=2:
                heapq.heappush(self.maxh , -heapq.heappop(self.minh))
        
        else:
            
            if len(self.minh) - len(self.maxh) >=1:
                heapq.heappush(self.maxh , -num)
            else:
                heapq.heappush(self.minh , num)

    def findMedian(self) -> float:
        if len(self.minh) == len(self.maxh):
            return (self.minh[0] - self.maxh[0] )/2
        elif len(self.minh) > len(self.maxh):
            return self.minh[0]
        else:
            return -self.maxh[0]
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()