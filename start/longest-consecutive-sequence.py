class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        count =0
        
        
        for num in nums:
            
            if num-1 not in num_set:
                curr =1
                i = num+1
                while i in num_set:
                    curr+=1
                    i+=1
                    
                count= max(count,curr)
                
                
        return count
        