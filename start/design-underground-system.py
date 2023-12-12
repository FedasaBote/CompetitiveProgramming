class UndergroundSystem:

    def __init__(self):
        self.check_in ={}
        self.check_out ={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] =[stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station_name , t_ = self.check_in[id]
        total_time = t - t_
        if (station_name,stationName) not in self.check_out:
            self.check_out[(station_name,stationName)] =[]
        self.check_out[(station_name,stationName)].append(total_time)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.check_out[(startStation,endStation)])/len(self.check_out[(startStation,endStation)])
        
        
            


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)