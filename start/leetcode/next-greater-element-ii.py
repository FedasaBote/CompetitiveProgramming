class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        nums = nums + nums
    
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                val = stack.pop()
                if ans[val%n] == -1:
                    ans[val%n] = nums[i]

            stack.append(i)

        return ans
        