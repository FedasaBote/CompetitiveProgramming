class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        nums= [(nums[i],i) for i in range(len(nums))]
        nums.sort()
        ans = [0]*len(nums)
        print(nums)
        for i in range(len(nums)):
            
            num ,idx = nums[i]
            if i>0 and nums[i-1][0] == nums[i][0]:
                ans[idx] = ans[nums[i-1][1]]
            
            else:
                ans[idx] = i
                
        return ans
        
        