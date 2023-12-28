class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def comp(val1, val2):
            val1= str(val1)
            val2 = str(val2)
            res1 = val1+val2
            res2 = val2+val1
            
            return res1>res2
        for i in range(len(nums)):
            for j in range(1,len(nums)-i):
                if comp(nums[j-1],nums[j]):
                    nums[j-1],nums[j] = nums[j],nums[j-1]
                    
        revs = list(map(str,nums[::-1]))
        ans = "".join(revs)
        if not ans.lstrip("0"):
            return "0"
        return ans
                
                
        
                