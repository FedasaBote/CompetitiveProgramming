class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        ans = [-1]*n
        map_ = {}
        for idx, num in enumerate(nums1):
            map_[num] = idx
        stack = []
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                val = stack.pop()
                if val in map_:
                    ans[map_[val]] = nums2[i]

            stack.append(nums2[i])

        return ans
        