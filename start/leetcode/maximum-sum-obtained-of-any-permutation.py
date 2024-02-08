class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        freq =[0]*len(nums)
        
        for i in range(len(requests)):
            start, end = requests[i]
            freq[start]+=1
            if end +1 <len(nums):
                freq[end+1]-=1
                
        for i in range(1,len(freq)):
            freq[i]+=freq[i-1]
            
        
        nums.sort()
        freq.sort()
        
        ans = 0
        for i in range(len(freq)):
            ans += (freq[i]*nums[i])%1000000007
            
        return ans%1000000007
        