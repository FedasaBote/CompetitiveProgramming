class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        cur_sum = 0
        for idx, num in enumerate(nums):
            cur_sum += num
            ans = max(ans, ceil(cur_sum/(idx+1)))
        return ans
       