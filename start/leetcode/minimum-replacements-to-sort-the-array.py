class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:

        c = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > nums[i+1]:
                d = math.ceil(nums[i]/nums[i+1])
                c += d-1
                nums[i] = nums[i]//d
        return c
        