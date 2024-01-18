class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        startIndex=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[startIndex]=nums[i]
                startIndex+=1
        return startIndex
        