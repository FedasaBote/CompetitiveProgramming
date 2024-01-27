class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        ans  = [0]*(n+1)
        
        for i in range(len(bookings)):
            first,last,seat = bookings[i]
            ans[first-1] += seat
            ans[last] += -seat
            
        for i in range(len(ans)-1):
            ans[i+1]+=ans[i]
            
        ans.pop()
        return ans
        
        
        
        
        