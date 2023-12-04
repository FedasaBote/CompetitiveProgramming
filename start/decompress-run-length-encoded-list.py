class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        prev=[]
        i=0
        
        while i<len(nums):
            freq = nums[i]
            val = nums[i+1]
            prev = prev+[val]*freq
            i+=2
            
        return prev