class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0]!= 0:
            return 0
        
        
        missing = -1
        
        for i in range(1,len(nums)):
            if nums[i]-1==nums[i-1]:
                continue
                
            missing= nums[i]-1
            
        return missing if missing!=-1 else len(nums)
        