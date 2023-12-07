class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even =[]
        odd =[]
        for i in range(len(nums)):
            if nums[i]>=0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
       
        j =0
        for i in range(0,len(nums),2):
            nums[i] = even[j]
            j+=1
           
        j=0
        for i in range(1,len(nums),2):
            nums[i] = odd[j]
            j+=1
            
        return nums
            
                
                
        