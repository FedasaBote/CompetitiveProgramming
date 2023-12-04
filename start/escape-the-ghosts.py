class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        
        distance = abs(target[0])+abs(target[1])
        
        for point in ghosts:
            dist =abs(target[0]-point[0])+abs(target[1]-point[1])
            if dist<= distance:
                return False
            
            
        return True
        