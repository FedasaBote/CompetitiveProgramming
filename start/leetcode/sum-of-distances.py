class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        map_ = {}
        
        for idx,val in enumerate(nums):
            if val not in map_:
                map_[val] =[]
                
            map_[val].append(idx)
            
        ans = [0]*len(nums) 
        for num,val in map_.items():
            suffix = sum(val)
            prefix = 0
            p =0
            s = len(val)
            
            for i in val:
                p += 1
                s -= 1
                prefix += i
                suffix -= i
                ans[i] = -prefix + p*i - s*i + suffix
                
        return ans
            
            
                
                
            
            
        
        
        