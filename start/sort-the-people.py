class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(1,len(names)):
            value = heights[i]
            
            j=i -1
            
            while  j>=0 and heights[j]<value:
                heights[j],heights[j+1] = heights[j+1],heights[j]
                names[j] , names[j+1]  = names[j+1] ,names[j]
                j-=1
                
        return names