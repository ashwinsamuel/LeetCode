class UndergroundSystem:

    def __init__(self):
        self.checked = {}
        self.avg = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checked[id] = (stationName , t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        src , start = self.checked[id]
        self.checked[id] = 0
        
        tsum , n = self.avg.get((src , stationName), (0,0))
        tsum += (t-start)
        n+=1
        self.avg[(src , stationName)] = (tsum,n)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg[(startStation , endStation)][0] / self.avg[(startStation , endStation)][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)