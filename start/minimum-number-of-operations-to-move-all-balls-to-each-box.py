class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        
        ans=[]
        
        for i in range(len(boxes)):
            res =0
            for j in range(len(boxes)):
                if boxes[j]=="1":
                    res+=abs(i-j)
                    
            ans.append(res)
            
        return ans
        
        