class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        fill = capacity
        ans =0
        for i in range(len(plants)):
            if (fill>=plants[i]):
                ans+=1
                fill-=plants[i]
                if i+1<len(plants) and fill<plants[i+1]:
                    ans+=((i+1)*2)
                    fill=capacity
                    
        return ans
            