class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        
        set_ =set()
        
        for range_ in ranges:
            for j in range(range_[0],range_[1]+1):
                set_.add(j)
                
        for i in range(left,right+1):
            if not i in set_:
                return False
            
        return True
                
        