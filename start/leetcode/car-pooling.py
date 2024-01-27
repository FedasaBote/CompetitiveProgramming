class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = len(trips)
        max_ = trips[0][2]
        
        for trip in trips:
            max_ = max(max_,trip[2])
        ans = [0]*(max_ +2)
        
        for i in range(len(trips)):
            passengers , start, end = trips[i]
            ans[start] += passengers
            ans[end] += -passengers
            
        for i in range(len(ans)-1):
            if ans[i]>capacity:
                return False
            ans[i+1]+=ans[i]
            
        return True
            
        
        