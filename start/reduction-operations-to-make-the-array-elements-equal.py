class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        
        num_op =0
        prev = 0
        idx = 0
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                idx += 1
                prev += idx
            else:
                prev+=idx
                
                
                
        return prev
        