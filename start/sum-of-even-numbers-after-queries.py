class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        total_evn=0
        
        for num in nums:
            if num%2==0:
                total_evn+=num
                
        ans =[]
        for query in queries:
            idx = query[1]
            val = query[0]
            result = val + nums[idx]
            
            if result%2==0 and val%2!=0:
                total_evn += result
                
            elif result%2==0:
                total_evn+=val
                
            elif result%2!=0 and nums[idx]%2==0:
                total_evn-= nums[idx]
                
            nums[idx]= result
            ans.append(total_evn)
            
            
        return ans