class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        times = len(nums)//3
        nums.sort()
        count =0
        ans =[]
        for i in range(len(nums)):
            if count==0:
                count =1
            elif i>0 and nums[i-1]==nums[i]:
                count+=1
            else:
                count=1
                
            if (not ans and count>times) or (count>times and ans[-1]!=nums[i]):
                ans.append(nums[i])
                
        return ans
                
        
        
        