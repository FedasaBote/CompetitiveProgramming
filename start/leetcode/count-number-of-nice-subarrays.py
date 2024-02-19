from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        odd_count = 0
        odd_counts = [0] * (len(nums) + 1)
        odd_counts[0] = 1  # Initialize with 1 to handle subarrays starting from index 0

        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            if odd_count >= k:
                count += odd_counts[odd_count - k]
            odd_counts[odd_count] += 1

        return count