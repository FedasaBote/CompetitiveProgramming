class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        ans =[]
        
        ones=nums.count(1)
        zeros = 0
        n = len(nums)
        for i in range(n):
            ans.append(zeros+ones)
            if nums[i]==0:
                zeros+=1
            else:
                ones-=1
        ans.append(zeros+ones)       
        m = max(ans)
        
        
        res =[]
        for i in range(len(ans)):
            if ans[i] ==m:
                res.append(i)
                
                
        return res
        