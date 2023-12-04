class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        total= sum(distance)
        ans =0
        
        for i in range(min(start,destination),max(start,destination)):
            ans+=distance[i]
            
        return min(ans,total-ans)
        