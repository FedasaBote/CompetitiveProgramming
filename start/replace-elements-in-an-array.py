class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mp ={}
        
        for i in range(len(nums)):
            mp[nums[i]]=i
            
            
        for op in operations:
            idx = mp[op[0]]
            del mp[op[0]]
            mp[op[1]]= idx
            
        ans =[0]*len(mp)
        
        for num in mp:
            ans[mp[num]]= num
            
        return ans