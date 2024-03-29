class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def helper(nums,start,end):
            if start==end:
                return nums[start]
            
            return max(nums[start]-helper(nums,start+1,end),nums[end]-helper(nums,start,end-1))

        return helper(nums,0,len(nums)-1)>=0