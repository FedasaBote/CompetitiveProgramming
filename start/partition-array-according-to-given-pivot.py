class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less =[]
        more =[]
        
        equal =[]
        
        for i in range(len(nums)):
            if nums[i] < pivot:
                less.append(nums[i])
            elif nums[i]==pivot:
                equal.append(nums[i])
            else:
                more.append(nums[i])
                
        result=less+equal+more
        
        for i in range(len(nums)):
            nums[i]=result[i]
            
        return nums
        