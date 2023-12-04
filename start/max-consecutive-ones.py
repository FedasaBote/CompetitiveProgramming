class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count =0
        max_ =0
        
        for i in nums:
            if i==0:
                count=0
            else:
                count+=1
                
            max_= max(count,max_)
        return  max_