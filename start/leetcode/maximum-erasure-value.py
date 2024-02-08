
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()
        left = 0
        curr_sum = 0
        max_sum = 0
        
        for right in range(n):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            
            seen.add(nums[right])
            curr_sum += nums[right]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum