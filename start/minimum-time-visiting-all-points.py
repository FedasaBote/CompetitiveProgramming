class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        prev=points[0]
        total =0
        for point in points[1:]:
            x = 1 if prev[0]<point[0] else -1
            y = 1 if prev[1]<point[1] else -1
            while point[0]!=prev[0] and point[1]!=prev[1]:
                total+=1
                prev[0]+=x
                prev[1]+=y
                
            total+=(abs(point[0]-prev[0])+abs(point[1]-prev[1]))
            prev=point
            
        return total
            
            