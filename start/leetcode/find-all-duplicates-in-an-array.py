class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        i = 0
        arr = nums
        ans =set()
        while i < len(arr):
            idx = arr[i] - 1
            if i != idx:
                if arr[idx] == arr[i]:
                    ans.add(nums[i])
                    i +=1
                    continue
                arr[i],arr[idx] = arr[idx],arr[i]
            else:
                i += 1
                
        return ans
            