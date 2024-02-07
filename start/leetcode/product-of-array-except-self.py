class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        forward  = [0]*len(nums)
        reverse  = [0]*len(nums)
        forward[0] =1
        reverse[-1] =1
        
        for i in range(1,len(nums)):
            forward[i]= nums[i-1]*forward[i-1]
            reverse[len(nums)-1-i]=nums[len(nums)-i]*reverse[len(nums)-i]
            
        ans = [0]*len(nums)
        
        for i in range(len(nums)):
            ans[i] = forward[i]*reverse[i]
            
        return ans
            