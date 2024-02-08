class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        pre_sum = [0]*len(nums)
        suf_sum = [0]*len(nums)
        n = len(nums)
        
        for i in range(1,n):
            pre_sum[i] = pre_sum[i-1]+ nums[i-1]
            suf_sum[n-1-i] = suf_sum[n-i] + nums[n-i]
            
        ans =[0]*n
        
        for i in range(n):
            ans[i] = nums[i]*i - pre_sum[i] + suf_sum[i] - nums[i]*(n-1-i)
            
        return ans
        